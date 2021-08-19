import sys
import copy
DEBUG = False
if DEBUG:
    inf = open('input.txt')
else:
    inf = sys.stdin
(N, M) = list(map(int, inf.readline().split(' ')))
n_items = list(map(int, inf.readline().split(' ')))
sales = []
for _ in range(M):
    sale = list(map(int, inf.readline().split(' ')))
    sales.append(sale)
sales = sorted(sales, key=lambda x: x[0], reverse=True)


def can_buy_in(dday):
    used = 0
    money_left = dday
    items = n_items[:]
    for (sale_day, sale_type) in sales:
        if sale_day > dday:
            continue
        if money_left > sale_day:
            money_left = sale_day
        can_buy = min(items[sale_type - 1], money_left)
        used += can_buy
        items[sale_type - 1] -= can_buy
        money_left -= can_buy
        if money_left == 0:
            break
    need_money_for_rest = sum(items) * 2
    return need_money_for_rest + used <= dday


total_items = sum(n_items)
low = total_items
high = total_items * 2
while low <= high:
    mid = (low + high) // 2
    if can_buy_in(mid):
        high = mid - 1
    else:
        low = mid + 1
print(low)

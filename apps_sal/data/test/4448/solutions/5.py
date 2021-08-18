import sys

DEBUG = False

if DEBUG:
    inf = open("input.txt")
else:
    inf = sys.stdin

N, M = list(map(int, inf.readline().split(' ')))
n_items = list(map(int, inf.readline().split(' ')))
sales = []
for _ in range(M):
    sale = list(map(int, inf.readline().split(' ')))
    sales.append(sale)

sales = sorted(sales, key=lambda x: x[0])

last_sales = {k: -1 for k in range(N + 1)}
final_sol = 99999999

for i in range(M):
    sale_day, sale_type = sales[i]
    last_sales[sale_type] = sale_day
    if i != M - 1:
        if sales[i + 1][0] == sale_day:
            continue

    total = 0
    lasts = last_sales.items()
    lasts = sorted(lasts, key=lambda x: x[1])
    burle = 0
    before_lastday = -1
    for stype, last_sday in lasts:
        if stype == 0:
            continue
        if last_sday == -1:
            total += n_items[stype - 1] * 2
            continue

        if before_lastday == -1:
            burle = last_sday
        else:
            burle += last_sday - before_lastday
        before_lastday = last_sday

        bought = min(burle, n_items[stype - 1])
        left = n_items[stype - 1] - bought
        burle -= bought
        total += bought + 2 * left

    sol = max(sale_day, total)
    if final_sol > sol:
        final_sol = sol

print(final_sol)

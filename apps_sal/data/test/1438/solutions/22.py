import math

n, k = list(map(int, input().split()))
req_ingr = list(map(int, input().split()))
hvng_ingr = list(map(int, input().split()))


def if_sum_bigger(count):
    summ = 0
    for i in range(n):
        summ += max(0, count * req_ingr[i] - hvng_ingr[i])
    if summ <= k:
        return True
    else:
        return False

l = 0
r = 2 * (10 ** 9) + 1

while (r > l):
    m = math.floor((r + l) / 2)
    if if_sum_bigger(m):
        l = m + 1
    else:
        r = m
m = math.floor((r + l) / 2)
if if_sum_bigger(m):
    print(m)
else:
    print(m-1)


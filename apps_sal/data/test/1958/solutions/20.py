from math import ceil

n, p = list(map(int, input().split()))
bs = [input() for i in range(n)]

apples = 0
money = 0
for b in bs[::-1]:
    apples *= 2
    if b == 'halfplus':
        apples += 0.5
        apples = ceil(apples)

    money += apples / 2 * p

print(int(money))

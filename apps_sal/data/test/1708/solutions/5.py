(n, m) = list(map(int, input().split()))
dish = list(map(int, input().split()))
cost = list(map(int, input().split()))
scost = []
for i in range(n):
    scost.append([cost[i], dish[i], i])
scost = sorted(scost)
cur = 0
for i in range(m):
    (x, y) = list(map(int, input().split()))
    x -= 1
    price = 0
    if dish[x] >= y:
        price += cost[x] * y
        dish[x] -= y
        y = 0
    else:
        price += cost[x] * dish[x]
        y -= dish[x]
        dish[x] = 0
        while y > 0:
            try:
                tmp = scost[cur][-1]
                if dish[tmp] >= y:
                    price += cost[tmp] * y
                    dish[tmp] -= y
                    y = 0
                else:
                    price += cost[tmp] * dish[tmp]
                    y -= dish[tmp]
                    dish[tmp] = 0
                    cur += 1
            except IndexError:
                price = 0
                y = 0
    print(price)

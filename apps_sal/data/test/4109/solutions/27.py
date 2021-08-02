n, m, x = map(int, input().split())
c = [list(map(int, input().split())) for _ in range(n)]
prices = []
for i in range(2**n):
    buy = [[] for _ in range(m + 1)]
    for j in range(n):
        if ((i >> j) & 1):
            for k in range(m + 1):
                buy[k].append(c[j][k])
    for k in range(1, m + 1):
        if sum(buy[k]) < x:
            break
    else:
        prices.append(sum(buy[0]))
if len(prices) == 0:
    print(-1)
else:
    print(min(prices))

N, M = list(map(int, input().split()))
price = [[] for i in range(N)]
for i in range(N):
    a, b = list(map(int, input().split()))
    price[i] = [a, b]
price.sort()
m = 0
money = 0
for i in range(N):
    if m + price[i][1] < M:
        money += price[i][0] * price[i][1]
        m += price[i][1]
    else:
        money += price[i][0] * (M - m)
        break
print(money)

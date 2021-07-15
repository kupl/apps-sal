JPY = 1
BTC = 380000
n = int(input())
ans = 0
for i in range(n):
    x,u = map(str,input().split())
    if u == 'BTC':
        tmp = float(x) * BTC
    else:
        tmp = int(x) * JPY
    ans += tmp
print(ans)

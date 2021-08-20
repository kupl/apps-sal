N = int(input())
ans = 0
for i in range(N):
    (x, u) = input().split()
    x = float(x)
    if u == 'BTC':
        ans += 380000.0 * x
    elif u == 'JPY':
        ans += x
print(ans)

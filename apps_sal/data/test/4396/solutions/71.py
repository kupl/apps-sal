N = int(input())
ans = 0.0
r = 380000.0
for i in range(N):
    (x, u) = input().split()
    x = float(x)
    if u == 'JPY':
        ans += x
    if u == 'BTC':
        ans += r * float(x)
print(ans)

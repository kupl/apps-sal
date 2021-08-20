N = int(input())
ans = 0
for _ in range(N):
    (x, u) = input().split()
    if u == 'JPY':
        ans += int(x)
    if u == 'BTC':
        ans += float(x) * 380000.0
print(ans)

N = int(input())

ans = 0
for i in range(N):
    x, u = input().split()
    if u == 'JPY':
        ans += int(x)
    if u == 'BTC':
        ans += 380000.0 * float(x)

print(ans)

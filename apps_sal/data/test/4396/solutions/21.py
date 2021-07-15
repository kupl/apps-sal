N = int(input())

ans = 0

for _ in range(N):
    x,u = input().split()
    x = float(x)
    if u == 'BTC':
        ans += 380000*x
    else:
        ans += x

print(ans)

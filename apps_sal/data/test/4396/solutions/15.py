n = int(input())
ans = 0
for _ in range(n):
    (x, u) = input().split()
    x = float(x)
    if u == 'BTC':
        x *= 380000
    ans += x
print(ans)

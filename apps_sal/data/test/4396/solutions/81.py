N = int(input())
ans = 0
for i in range(N):
    (x, u) = map(str, input().split())
    x = float(x)
    if u == 'JPY':
        ans += x
    else:
        ans += x * 380000.0
print(ans)

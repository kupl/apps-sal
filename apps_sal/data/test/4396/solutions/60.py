N = int(input())
ans = 0
for i in range(N):
    x, u = map(str, input().split())
    if u == 'JPY':
        ans += int(x)
    else:
        ans += float(x) * 380000
print(ans)

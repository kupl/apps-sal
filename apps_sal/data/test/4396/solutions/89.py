n = int(input())
a = [list(input().split()) for _ in range(n)]
ans = 0
for i in range(n):
    if a[i][1] == 'BTC':
        ans += float(a[i][0]) * 380000
    else:
        ans += float(a[i][0])
print(ans)

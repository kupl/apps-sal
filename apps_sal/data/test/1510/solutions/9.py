(n, m) = map(int, input().split())
a = sorted(map(int, input().split()))
b = sorted(map(int, input().split()))[::-1]
ans = 0
for i in range(min(n, m)):
    if b[i] > a[i]:
        ans += b[i] - a[i]
print(ans)

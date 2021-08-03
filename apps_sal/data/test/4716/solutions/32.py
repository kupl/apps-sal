n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort(reverse=True)

ans = 0
for i in range(k):
    ans += a[i]
print(ans)

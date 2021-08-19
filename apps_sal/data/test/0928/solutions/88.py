(n, k) = map(int, input().split())
a = list(map(int, input().split()))
ans = 0
ref = 0
cnt = 0
for i in range(n):
    ref += a[i]
    while ref >= k:
        ref -= a[cnt]
        cnt += 1
    ans += cnt
print(ans)

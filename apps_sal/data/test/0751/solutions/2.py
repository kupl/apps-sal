(n, m) = map(int, input().split())
a = list(map(int, input().split()))
cnt = 0
cur = 0
for i in range(n):
    if a[i] <= m - cur:
        cur += a[i]
    else:
        cnt += 1
        cur = a[i]
print(cnt + 1)

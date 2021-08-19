(n, x) = map(int, input().split())
a = list(map(int, input().split()))
cnt = 0
if a[0] > x:
    cnt += a[0] - x
    a[0] -= a[0] - x
for i in range(n - 1):
    if a[i] + a[i + 1] > x:
        cnt += a[i] + a[i + 1] - x
        a[i + 1] -= a[i] + a[i + 1] - x
print(cnt)

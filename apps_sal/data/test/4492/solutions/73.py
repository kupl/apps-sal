(n, x) = list(map(int, input().split()))
a = list(map(int, input().split()))
cnt = 0
for i in range(n):
    if a[i] > x:
        cnt += a[i] - x
        a[i] = x
for i in range(n - 1):
    dif = a[i] + a[i + 1] - x
    if dif > 0:
        a[i + 1] -= dif
        cnt += dif
print(cnt)

(N, x) = map(int, input().split())
a = list(map(int, input().split()))
cnt = 0
for i in range(1, N):
    if a[i - 1] > x:
        b = a[i - 1] - x
        cnt += b
        a[i - 1] -= b
    if a[i - 1] + a[i] > x:
        b = a[i - 1] + a[i] - x
        cnt += b
        a[i] -= b
print(cnt)

n, x = list(map(int, input().split()))
a = list(map(int, input().split()))

cnt = max(0, a[0] - x)
a[0] -= cnt
for i in range(1, n):
    cnt_now = max(0, a[i - 1] + a[i] - x)
    a[i] -= cnt_now
    cnt += cnt_now

print(cnt)

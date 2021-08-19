(n, k) = map(int, input().split())
a = list(map(int, input().split()))
cnt = 0
for i in range(1, n):
    if a[i] + a[i - 1] < k:
        cnt += k - a[i] - a[i - 1]
        a[i] += k - a[i] - a[i - 1]
print(cnt)
print(' '.join(map(str, a)))

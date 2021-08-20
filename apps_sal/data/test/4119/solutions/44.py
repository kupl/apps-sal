(n, m) = map(int, input().split())
a = sorted(list(map(int, input().split())))
dst = [0] * (m - 1)
for i in range(m - 1):
    dst[i] = abs(a[i + 1] - a[i])
dst.sort(reverse=True)
print(sum(dst[n - 1:]))

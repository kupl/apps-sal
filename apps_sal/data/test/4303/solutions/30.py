import bisect
(n, k) = list(map(int, input().split()))
x = list(map(int, input().split()))
c = bisect.bisect_left(x, 0)
mt = 2 * 10 ** 8
for i in range(n - k + 1):
    if i + k < c:
        continue
    mt = min(mt, 2 * abs(x[i]) + abs(x[i + k - 1]), abs(x[i]) + 2 * abs(x[i + k - 1]))
    if i + k - 1 == c - 1:
        mt = min(mt, abs(x[i]))
    if i == c:
        mt = min(mt, x[i + k - 1])
if n == k:
    if c != n and c != 0:
        mt = min(2 * abs(x[0]) + x[-1], 2 * x[-1] + abs(x[0]))
    else:
        mt = max(abs(x[0]), abs(x[-1]))
print(mt)

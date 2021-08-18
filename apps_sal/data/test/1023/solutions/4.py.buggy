from bisect import bisect_left
n, m, ta, tb, k = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
if n <= k:
    print(-1)
    return

ma = 0
for i in range(k + 1):
    p = a[i]
    q = k - i
    j = bisect_left(b, p + ta)
    if j + q >= m:
        print(-1)
        return

    ma = max(ma, b[j + q] + tb)

print(ma)

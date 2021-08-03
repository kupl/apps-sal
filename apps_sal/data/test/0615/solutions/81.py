from itertools import accumulate as acc
from bisect import bisect_left as bl


def ans(n):
    tmp = 0
    for i in range(N):
        tmp += abs(a[i] - a[n - 1])
    return tmp


N = int(input())
a = list(acc(map(int, input().split())))

ans = a[-1]
p = 0
q = 2
for j in range(1, N - 2):
    q = max(q, j + 1)
    while p < j - 1 and abs(a[j] - a[p] * 2) > abs(a[j] - a[p + 1] * 2):
        p += 1
    while q < N - 2 and abs(a[j] + a[N - 1] - a[q] * 2) > abs(a[j] + a[N - 1] - a[q + 1] * 2):
        q += 1

    x = [a[p], a[j] - a[p], a[q] - a[j], a[N - 1] - a[q]]
    ans = min(ans, max(x) - min(x))

print(ans)

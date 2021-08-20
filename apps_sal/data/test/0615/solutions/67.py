from itertools import accumulate as acc
from bisect import bisect_left as bl


def ans(n):
    tmp = 0
    for i in range(N):
        tmp += abs(a[i] - a[n - 1])
    return tmp


N = int(input())
a = list(map(int, input().split()))
a = list(acc(a))
ans = 10 ** 18
for j in range(1, N - 2):
    x = a[j] / 2
    p = bl(a, x)
    if p == j:
        p -= 1
    elif p > 0 and x - a[p - 1] < a[p] - x:
        p -= 1
    y = (a[j] + a[N - 1]) / 2
    q = bl(a, y)
    if q == N - 1:
        q -= 1
    elif q > j + 1 and y - a[q - 1] < a[q] - y:
        q -= 1
    (P, Q, R, S) = (a[p], a[j] - a[p], a[q] - a[j], a[N - 1] - a[q])
    ans = min(ans, max(P, Q, R, S) - min(P, Q, R, S))
print(ans)

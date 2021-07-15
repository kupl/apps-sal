from fractions import gcd
from collections import defaultdict

N, X, D = list(map(int, input().split()))

if D == 0:
    if X == 0:
        ans = 1
    else:
        ans = N + 1
else:
    if D < 0:
        X = -X
        D = -D
    g = gcd(X, D)
    X //= g
    D //= g

    AN = X + D * (N - 1)

    intervals_dict = defaultdict(list)
    for k in range(N + 1):
        start = k * (2 * X + (k - 1) * D) // 2
        end = k * (2 * AN - (k - 1) * D) // 2

        intervals_dict[start % D].append((start // D, end // D + 1))

    ans = 0
    for k, v in list(intervals_dict.items()):
        v.sort()

        current_stop = -float("inf")
        for start, stop in v:
            ans += max(stop, current_stop) - max(start, current_stop)
            current_stop = max(current_stop, stop)

print(ans)


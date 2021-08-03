

import bisect

for _ in range(int(input())):

    n, k = map(int, input().split())

    x = list(map(int, input().split()))
    y = input()
    x.sort()
    X = [bisect.bisect_right(x, x[i] + k) for i in range(n)]
    Y = [0]
    for i in range(n - 1, -1, -1):
        Y += [max(Y[-1], X[i] - i)]
    Y.reverse()
    ans = 0
    for i in range(n):
        ans = max(ans, X[i] - i + Y[X[i]])
    print(ans)

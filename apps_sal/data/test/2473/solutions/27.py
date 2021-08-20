from itertools import combinations
(N, K) = (int(x) for x in input().split())
Plot = [tuple((int(x) for x in input().split())) for _ in range(N)]
X = [p[0] for p in Plot]
Y = [p[1] for p in Plot]
X.sort()
Y.sort()
ans = 1e+21
for (x1, x2) in combinations(X, 2):
    for y1 in Y:
        y2 = [y for (x, y) in Plot if x1 <= x <= x2 and y1 <= y]
        if len(y2) < K:
            break
        y2.sort()
        S = (x2 - x1) * (y2[K - 1] - y1)
        ans = min(ans, S)
print(ans)

import bisect
(A, B, Q) = map(int, input().split())
(*S,) = [int(input()) for _ in range(A)]
(*T,) = [int(input()) for _ in range(B)]
(*X,) = [int(input()) for _ in range(Q)]
for x in X:
    sx = bisect.bisect(S, x)
    try:
        se = S[sx]
    except:
        se = S[-1]
    try:
        sw = S[sx - 1]
    except:
        sw = S[0]
    tx = bisect.bisect(T, x)
    try:
        te = T[tx]
    except:
        te = T[-1]
    try:
        tw = T[tx - 1]
    except:
        tw = T[0]
    routes = []
    for s in [se, sw]:
        for t in [te, tw]:
            routes.append(abs(s - x) + abs(t - s))
            routes.append(abs(t - x) + abs(s - t))
    print(min(routes))

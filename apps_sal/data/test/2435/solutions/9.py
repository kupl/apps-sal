T = int(input())
for _ in range(T):
    (N, X, M) = list(map(int, input().split()))
    LR = [tuple(map(int, input().split())) for i in range(M)]
    mn = mx = X
    for (l, r) in LR:
        if l > mx:
            continue
        if r < mn:
            continue
        mn = min(mn, l)
        mx = max(mx, r)
    print(mx - mn + 1)

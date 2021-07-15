for _ in range(int(input())):
    n = int(input())
    ans = 0
    adj = []
    a = tuple(map(int, input().split()))
    a1 = iter(a)
    next(a1)
    for ai, aj in zip(a, a1):
        if ai > -1 < aj:
            ans = max(ans, abs(ai - aj))
        elif ai != aj:
            adj.append(ai + aj + 1)
    min_adj, max_adj = (min(adj), max(adj)) if adj else (0, 0)
    print(max(ans, (max_adj - min_adj + 1) // 2), (min_adj + max_adj) // 2)


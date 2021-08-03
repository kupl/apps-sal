def solve():
    import sys
    input = sys.stdin.readline

    N, M = list(map(int, input().split()))
    adjL = [[] for _ in range(N)]
    adjLRev = [[] for _ in range(N)]
    outdegs = [0] * N
    for _ in range(M):
        s, t = list(map(int, input().split()))
        s, t = s - 1, t - 1
        adjL[s].append(t)
        adjLRev[t].append(s)
        outdegs[s] += 1

    probs = [0] * N
    expes = [0] * N
    probs[0] = 1
    for v in range(N):
        prob, expe, outdeg = probs[v], expes[v], outdegs[v]
        if prob != 0:
            num = expe / prob
            for v2 in adjL[v]:
                probs[v2] += prob / outdeg
                expes[v2] += prob * (num + 1) / outdeg

    probRevs = [0] * N
    expeRevs = [0] * N
    probRevs[-1] = 1
    for v in reversed(list(range(N))):
        prob, expe = probRevs[v], expeRevs[v]
        if prob != 0:
            num = expe / prob
            for v0 in adjLRev[v]:
                probRevs[v0] += prob / outdegs[v0]
                expeRevs[v0] += prob * (num + 1) / outdegs[v0]

    ans = expes[-1]
    for vRem in range(N - 1):
        if outdegs[vRem] == 1:
            continue
        values = []
        prob, expe, outdeg = probs[vRem], expes[vRem], outdegs[vRem]
        for v2 in adjL[vRem]:
            value = expe * probRevs[v2] + expeRevs[v2] * prob + prob * probRevs[v2]
            values.append(value)
        sumV = sum(values)
        ans2 = expes[-1] - sumV / outdeg
        for value in values:
            ans = min(ans, ans2 + (sumV - value) / (outdeg - 1))

    print(ans)


solve()

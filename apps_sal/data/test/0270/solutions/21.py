def main():
    n, m = list(map(int, input().split()))
    st = [list(map(int, input().split())) for _ in [0] * m]
    g = [[] for _ in [0] * n]
    [g[a - 1].append(b - 1) for a, b in st]
    toP = [0] * n
    toE = [0] * n
    fromE = [0] * n
    toP[0] = 1
    for i in range(n - 1):
        p = toP[i]
        if p > 0:
            toE[i] /= toP[i]
        e = toE[i]
        l = len(g[i])
        for j in g[i]:
            toP[j] += p / l
            toE[j] += (e + 1) * p / l
    for i in range(n - 2, -1, -1):
        l = len(g[i])
        for j in g[i]:
            fromE[i] += (fromE[j] + 1) / l
    allE = fromE[0]
    ans = fromE[0]
    tf = [toP[i] * ((toE[i] + 1) * len(g[i]) + sum([fromE[j] for j in g[i]]))
          for i in range(n)]
    for s, t in st:
        if g[s - 1]:
            l = len(g[s - 1])
            if l > 1:
                ans = min(allE + tf[s - 1] * (1 / (l - 1) - 1 / l) - toP[s - 1] *
                          (toE[s - 1] + 1 + fromE[t - 1]) / (l - 1), ans)
    print(ans)


main()

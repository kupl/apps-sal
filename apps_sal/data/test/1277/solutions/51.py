(N, S, T) = list(map(int, input().split()))
S -= 1
T -= 1
edges = [[] for _ in range(N)]
for _ in range(N - 1):
    (fr, to) = [int(a) - 1 for a in input().split()]
    edges[fr].append(to)
    edges[to].append(fr)


def calc(s):
    minDist = [10 ** 18] * N
    minDist[s] = 0
    st = [s]
    while st:
        now = st.pop()
        d = minDist[now] + 1
        for to in edges[now]:
            if minDist[to] > d:
                minDist[to] = d
                st.append(to)
    return minDist


minDistS = calc(S)
minDistT = calc(T)
ans = 0
for (s, t) in zip(minDistS, minDistT):
    if s <= t:
        ans = max(ans, t - 1)
print(ans)

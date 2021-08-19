import queue


def bfs(G, s):
    st = set()
    q = queue.Queue()
    st.add(s)
    q.put(s)
    while not q.empty():
        p = q.get()
        for (v, _) in G[p]:
            if not v in st:
                st.add(v)
                q.put(v)
    return st


def solve(G, st):
    n = len(G)
    score = [-float('inf')] * n
    score[0] = 0
    for i in range(n):
        f = True
        for s in range(n):
            for (t, u) in G[s]:
                if not s in st or not t in st:
                    continue
                if score[t] < score[s] + u:
                    f = False
                    score[t] = score[s] + u
        if f:
            break
        if i == n - 1:
            return 'inf'
    return score[n - 1]


def main():
    (n, m) = map(int, input().split())
    G = [[] for _ in range(n)]
    revG = [[] for _ in range(n)]
    for _ in range(m):
        (a, b, c) = map(int, input().split())
        (a, b) = (a - 1, b - 1)
        G[a].append([b, c])
        revG[b].append([a, c])
    st1 = bfs(G, 0)
    st2 = bfs(revG, n - 1)
    st = st1 & st2
    print(solve(G, st))


def __starting_point():
    main()


__starting_point()

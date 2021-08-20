import sys
sys.setrecursionlimit(10 ** 6)


def LI():
    return list(map(int, input().split()))


(N, M) = LI()
AB = [LI() for _ in range(M)]
link = [[] for _ in range(N)]
for (a, b) in AB:
    link[a - 1].append(b - 1)
impossible = [False] * N


def joint(v, visit):
    if impossible[v]:
        return None
    visit = visit + [v]
    for u in link[v]:
        if u in visit:
            i = visit.index(u)
            return visit[i:]
        t = joint(u, visit)
        if t is not None:
            return t
    impossible[v] = True
    return None


def solve(l):
    n = len(l)
    d = {l[i]: i for i in range(n)}
    for i in range(n):
        x = l[i]
        for y in link[x]:
            if y in d:
                j = d[y]
                if (i + 1) % n == j:
                    continue
                if j < i:
                    l = l[j:i + 1]
                else:
                    l = l[:i + 1] + l[j:]
                return solve(l)
    return l


def main():
    t = None
    for i in range(N):
        t = joint(i, [])
        if t is not None:
            break
    if t is None:
        print(-1)
        return
    ans = solve(t)
    print(len(ans))
    for x in ans:
        print(x + 1)


def __starting_point():
    main()


__starting_point()

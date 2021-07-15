def solve():
    n, m, k = list(map(int, input().split()))
    r = {}
    for _ in range(m):
        u, v, l = list(map(int, input().split()))
        if u not in r:
            r[u] = []
        if v not in r:
            r[v] = []
        r[u].append((v, l))
        r[v].append((u, l))
    a = set()
    s = [False] * (n + 1)
    if k > 0:
        a = set(map(int, input().split()))
    for a_ in a:
        s[a_] = True
    ans = float('inf')
    for a_ in a:
        if a_ not in r:
            continue
        for t in r[a_]:
            if s[t[0]]:
                continue
            ans = min(ans, t[1])

    print(-1 if ans == float('inf') else ans)


def main():
    solve()


def __starting_point():
    main()

__starting_point()

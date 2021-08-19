import sys
sys.setrecursionlimit(10 ** 7)


def dfs(G, F, crr, pre, ret, st):
    F[crr] = False
    if crr < 10 ** 5:
        ret[0] += 1
    else:
        ret[1] += 1
    for nxt in G[crr]:
        if nxt == pre:
            continue
        (p, q) = (crr, nxt)
        if q < p:
            (p, q) = (q, p)
        if not (p, q) in st:
            st.add((p, q))
            ret[2] += 1
        if F[nxt]:
            dfs(G, F, nxt, crr, ret, st)


def main():
    n = int(input())
    G = [[] for _ in range(2 * 10 ** 5)]
    for _ in range(n):
        (x, y) = map(int, input().split())
        (x, y) = (x - 1, y - 1 + 10 ** 5)
        G[x].append(y)
        G[y].append(x)
    F = [True] * (2 * 10 ** 5)
    ans = 0
    st = set()
    for i in range(2 * 10 ** 5):
        if F[i] and len(G[i]) > 0:
            tmp = [0] * 3
            dfs(G, F, i, -1, tmp, st)
            ans += tmp[0] * tmp[1] - tmp[2]
    print(ans)


def __starting_point():
    main()


__starting_point()

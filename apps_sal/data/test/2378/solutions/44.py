import sys
sys.setrecursionlimit(10 ** 7)

MOD = 10**9 + 7


def MOD_inv(a):
    b = MOD
    u = 1
    v = 0
    while b > 0:
        t = a // b
        a -= t * b
        a, b = b, a
        u -= t * v
        u, v = v, u
    u = u % MOD
    if u < 0:
        u += MOD
    return u


def cntNode(G, C, crr, pre):
    s = 0
    for i, nxt in enumerate(G[crr]):
        if nxt == pre:
            continue
        else:
            C[crr][i] = cntNode(G, C, nxt, crr)
            s += C[crr][i]
    return s + 1


def main():
    n = int(input())
    G = [[] for _ in range(n)]
    for _ in range(n - 1):
        a, b = map(int, input().split())
        a, b = a - 1, b - 1
        G[a].append(b)
        G[b].append(a)
    C = [[-1] * len(G[i]) for i in range(n)]
    idx = -1
    for i in range(n):
        if len(G[i]) == 1:
            idx = i
            break
    cntNode(G, C, idx, -1)
    for i in range(n):
        idx = -1
        s = 0
        for j, v in enumerate(C[i]):
            if v == -1:
                idx = j
            else:
                s += v
        if idx != -1:
            C[i][idx] = n - 1 - s
    s = 0
    pows = [0] * (n + 1)
    pows[0] = 1
    for i in range(1, n + 1):
        pows[i] = 2 * pows[i - 1] % MOD
    for i in range(n):
        p = pows[n - 1]
        for v in C[i]:
            p -= pows[v] - 1
        p -= 1
        p %= MOD
        s += p
        s %= MOD
    print(s * MOD_inv(pows[n]) % MOD)


def __starting_point():
    main()


__starting_point()

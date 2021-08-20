def main():
    (n, m, k) = list(map(int, input().split()))
    (F, B) = ({}, {})
    for i in range(1, n + 1):
        F[i] = []
        B[i] = []
    for _ in range(m):
        (a, b) = list(map(int, input().split()))
        F[a] += [b]
        F[b] += [a]
    for _ in range(k):
        (a, b) = list(map(int, input().split()))
        B[a] += [b]
        B[b] += [a]
    G = [0 for i in range(n)]
    g = 1
    M = {}
    for i in range(n):
        if G[i] != 0:
            continue
        m = 1
        G[i] = g
        que = [i + 1]
        while len(que) > 0:
            q = que.pop(0)
            for nv in F[q]:
                if G[nv - 1] != 0:
                    continue
                G[nv - 1] = g
                que.append(nv)
                m += 1
        M[g] = m
        g += 1
    ans = []
    for i in range(n):
        g = G[i]
        a = M[g]
        for b in B[i + 1]:
            if G[b - 1] == g:
                a -= 1
        a -= len(F[i + 1])
        a -= 1
        ans.append(a)
    print(' '.join([str(a) for a in ans]))


def __starting_point():
    main()


__starting_point()

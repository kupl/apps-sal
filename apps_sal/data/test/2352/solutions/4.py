import sys


def solve():
    (H, W) = map(int, sys.stdin.readline().split())
    G = [[ord(s) - 46 for s in sys.stdin.readline().strip()] for _ in range(H)]
    k = 0
    inf = 10 ** 9
    Stbw = [-inf] * 77
    Stsw = [inf] * 77
    Stbh = [-inf] * 77
    Stsh = [inf] * 77
    for (h, G1) in enumerate(G, 1):
        k = max(k, max(G1))
        for (w, g) in enumerate(G1, 1):
            if not g:
                continue
            Stbw[g] = max(Stbw[g], w)
            Stsw[g] = min(Stsw[g], w)
            Stbh[g] = max(Stbh[g], h)
            Stsh[g] = min(Stsh[g], h)
    if k == 0:
        return []
    A = []
    for j in range(k, 50, -1):
        if Stbw[j] == -inf and Stbh[j] == -inf:
            A.append(A[-1])
            continue
        bw = Stbw[j] == Stsw[j]
        bh = Stbh[j] == Stsh[j]
        if not bw and (not bh):
            return False
        if bw:
            w = Stbw[j] - 1
            for h in range(Stsh[j] - 1, Stbh[j]):
                if G[h][w] < j:
                    return False
        elif bh:
            h = Stbh[j] - 1
            for w in range(Stsw[j] - 1, Stbw[j]):
                if G[h][w] < j:
                    return False
        A.append((Stsh[j], Stsw[j], Stbh[j], Stbw[j]))
    return A[::-1]


def __starting_point():
    T = int(input())
    for _ in range(T):
        ans = solve()
        if ans is False:
            print('NO')
            continue
        print('YES')
        print(len(ans))
        for a in ans:
            print(*a)


__starting_point()

import sys
sys.setrecursionlimit(10 ** 7)


def main1(n, p, x):
    ki = [[] for _ in range(n)]
    for (i, v) in enumerate(p):
        v -= 1
        i += 1
        ki[i].append(v)
        ki[v].append(i)

    def dfs(p, v):
        ary = []
        bs = 1
        sa = 0
        mina = 0
        for nv in ki[v]:
            if nv != p:
                (a, b) = dfs(v, nv)
                if a == -1:
                    return (-1, -1)
                ary.append([a, b])
                nbs = 0
                nbs |= bs << a
                nbs |= bs << b
                mina += min(a, b)
                sa += a + b
                bs = nbs
        if mina > x[v]:
            return (-1, -1)
        for j in range(x[v], mina - 1, -1):
            if bs >> j & 1:
                return (x[v], sa - j)
        return (-1, -1)
    (a, b) = dfs(-1, 0)
    if a != -1:
        return True
    else:
        return False


def __starting_point():
    n = int(input())
    p = list(map(int, input().split()))
    x = list(map(int, input().split()))
    ret1 = main1(n, p, x)
    print('POSSIBLE' if ret1 else 'IMPOSSIBLE')


__starting_point()

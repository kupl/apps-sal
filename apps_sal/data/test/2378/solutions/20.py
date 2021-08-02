import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

ans = 0


def main(n, ab):
    ki = [[] for _ in range(n)]
    for a, b in ab:
        a, b = a - 1, b - 1
        ki[a].append(b)
        ki[b].append(a)
    mod = 10**9 + 7
    n2 = [1]
    for i in range(n):
        n2.append((n2[-1] * 2) % mod)

    def dfs1(v, p):
        ret = 0
        nonlocal ans
        ans += n2[n - 1] - 1
        for nv in ki[v]:
            if nv == p:
                continue
            x = dfs1(nv, v)
            ans -= n2[x] - 1
            ans -= n2[n - x] - 1
            ret += x
        ans %= mod
        return ret + 1
    dfs1(0, -1)
    allpat = pow(2, n, mod)
    nonlocal ans
    ans *= pow(allpat, mod - 2, mod)
    return ans % mod


n = int(input())
ab = [list(map(int, input().split())) for _ in range(n - 1)]
print((main(n, ab)))

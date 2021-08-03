import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)


def solve():
    MOD = 10**9 + 7

    N = int(input())
    adjL = [[] for _ in range(N)]
    for _ in range(N - 1):
        a, b = list(map(int, input().split()))
        a, b = a - 1, b - 1
        adjL[a].append(b)
        adjL[b].append(a)

    sizeSubtrees = [0] * N
    sizeAdjss = [[] for _ in range(N)]

    def dfs(vNow, vPar):
        sizeSubtrees[vNow] = 1
        for v2 in adjL[vNow]:
            if v2 == vPar:
                continue
            s = dfs(v2, vNow)
            sizeAdjss[vNow].append(s)
            sizeSubtrees[vNow] += s
        sizeAdjss[vNow].append(N - sizeSubtrees[vNow])
        return sizeSubtrees[vNow]

    dfs(0, -1)

    def getPows(base, n, MOD):
        pows = [1] * (n + 1)
        for x in range(1, n + 1):
            pows[x] = (pows[x - 1] * base) % MOD
        return pows
    pow2s = getPows(2, N, MOD)

    nums = [0] * N
    for v in range(N):
        num = pow2s[N - 1] - 1
        for sizeAdj in sizeAdjss[v]:
            num -= pow2s[sizeAdj] - 1
            num %= MOD
        nums[v] = num

    ans = sum(nums) % MOD * pow(pow2s[N], MOD - 2, MOD) % MOD
    print(ans)


solve()

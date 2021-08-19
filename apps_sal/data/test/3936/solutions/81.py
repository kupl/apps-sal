def solve():

    def dfs(p, prea, preb):
        if p == n:
            return 1
        if (p, prea, preb) in dp:
            return dp[p, prea, preb]
        ret = 0
        if s1[p] == s2[p]:
            for i in range(3):
                if i != prea and i != preb:
                    ret += dfs(p + 1, i, i)
        else:
            for i in range(3):
                for j in range(3):
                    if i != j and i != prea and (j != preb):
                        ret += dfs(p + 2, i, j)
        ret %= mod
        dp[p, prea, preb] = ret
        return ret
    n = int(input())
    s1 = input()
    s2 = input()
    mod = 10 ** 9 + 7
    dp = {}
    print(dfs(0, -1, -1))


solve()

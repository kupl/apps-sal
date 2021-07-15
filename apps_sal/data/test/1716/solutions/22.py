import sys
sys.setrecursionlimit(10010010)

def abc106_d():
    n, m, q = map(int, input().split())
    table = [[0]*(n+1) for _ in range(n+1)]
    for _ in range(m):
        l, r = map(int, input().split())
        table[l][r] += 1
    query = [tuple(map(int, input().split())) for _ in range(q)]

    dp = [[-1]*(n+1) for _ in range(n+1)]

    def calc(l, r):
        nonlocal dp
        if l == 0 or r == 0: return 0
        if dp[l][r] != -1: return dp[l][r]
        res = calc(l-1, r) + calc(l, r-1) - calc(l-1, r-1) + table[l][r]
        dp[l][r] = res
        return res

    for p, q in query:
        ans = calc(q, q) - calc(q, p-1) - calc(p-1, q) + calc(p-1, p-1)
        print(ans)

def __starting_point():
    abc106_d()
__starting_point()

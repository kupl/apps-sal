from collections import deque
import sys
INF = 10 ** 9
MOD = 10 ** 9 + 7
sys.setrecursionlimit(100000000)
input = sys.stdin.readline
MAXN = 2005
dp0 = [[-1] * MAXN for _ in range(MAXN)]
dp1 = [[-1] * MAXN for _ in range(MAXN)]


def dfs(i, j, p, z, w, a, n):
    if p == 0:
        if dp0[i][j] != -1:
            return dp0[i][j]
        if i == n:
            if j == 0:
                return abs(w - a[-1])
            return abs(a[j - 1] - a[-1])
        ans = 0
        for k in range(i, n):
            ans = max(ans, dfs(k + 1, k, 1, z, w, a, n))
        if i == 1:
            ans = max(ans, abs(a[-1] - w))
        else:
            ans = max(ans, abs(a[-1] - a[i - 1]))
        dp0[i][j] = ans
        return ans
    elif p == 1:
        if dp1[i][j] != -1:
            return dp1[i][j]
        if i == n:
            if j == 0:
                return abs(z - a[-1])
            return abs(a[j - 1] - a[-1])
        ans = INF
        for k in range(i, n):
            ans = min(ans, dfs(k + 1, k, 0, z, w, a, n))
        if i == 1:
            ans = min(ans, abs(a[-1] - z))
        else:
            ans = min(ans, abs(a[-1] - a[i - 1]))
        dp1[i][j] = ans
        return ans


def main():
    (n, z, w) = map(int, input().split())
    a = list(map(int, input().split()))
    ans = dfs(1, 0, 0, z, w, a, n)
    print(ans)


def __starting_point():
    main()


__starting_point()

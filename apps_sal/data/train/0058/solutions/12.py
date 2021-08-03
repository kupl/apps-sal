import sys
input = sys.stdin.readline


def main():
    ans = []
    memo = [[[-1 for _ in range(51)] for _ in range(31)] for _ in range(31)]

    def solve(n, m, k):
        if n * m == k or k == 0:
            return 0
        if memo[n][m][k] > -1:
            return memo[n][m][k]
        if memo[m][n][k] > -1:
            memo[n][m][k] = memo[m][n][k]
            return memo[n][m][k]
        r = float('inf')
        for i in range(k + 1):
            for j in range(1, max(m, n)):
                if m > j:
                    r = min(r, n**2 + solve(j, n, i) + solve(m - j, n, k - i))
                if n > j:
                    r = min(r, m**2 + solve(m, j, i) + solve(m, n - j, k - i))
        memo[n][m][k] = r
        return r
    for _ in range(int(input())):
        n, m, k = map(int, input().split())
        ans.append(str(solve(n, m, k)))
    print('\n'.join(ans))


main()

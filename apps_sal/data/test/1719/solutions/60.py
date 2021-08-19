def solve(N):
    mod = 10 ** 9 + 7
    memo = [{} for _ in range(N + 1)]

    def check(last4):
        for i in range(4):
            x = list(last4)
            if i > 0:
                (x[i], x[i - 1]) = (x[i - 1], x[i])
            if ''.join(x).count('AGC') >= 1:
                return False
        return True

    def dfs(memo, digit, last3):
        if last3 in memo[digit]:
            return memo[digit][last3]
        if digit == 0:
            return 1
        re = 0
        for c in 'AGCT':
            if check(last3 + c):
                re = (re + dfs(memo, digit - 1, last3[1:] + c)) % mod
        memo[digit][last3] = re
        return re
    print(dfs(memo, N, 'TTT'))


def __starting_point():
    N = int(input())
    solve(N)


__starting_point()

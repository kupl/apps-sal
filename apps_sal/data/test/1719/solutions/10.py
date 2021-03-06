def ok(last4):
    for i in range(4):
        t = list(last4)
        if i >= 1:
            (t[i - 1], t[i]) = (t[i], t[i - 1])
        if 'AGC' in ''.join(t):
            return False
    return True


def main():
    MOD = 10 ** 9 + 7
    N = int(input())
    memo = [{} for _ in range(N + 1)]

    def dfs(cur, last3):
        if last3 in memo[cur]:
            return memo[cur][last3]
        if cur == N:
            return 1
        ret = 0
        for c in 'ACGT':
            if ok(last3 + c):
                ret = (ret + dfs(cur + 1, last3[1:] + c)) % MOD
        memo[cur][last3] = ret
        return ret
    print(dfs(0, 'TTT'))


def __starting_point():
    main()


__starting_point()

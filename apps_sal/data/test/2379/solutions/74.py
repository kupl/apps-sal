def do_solve(n, k, c, s):
    dp = [0 for i in range(n)]
    for i in range(n):
        dp[i] = 1 if s[i] == 'o' else 0
        if i - c - 1 >= 0:
            dp[i] = max(dp[i], dp[i - c - 1] + 1 if s[i] == 'o' else 0)
        if i - 1 >= 0:
            dp[i] = max(dp[i], dp[i - 1])
    return dp


def solve(n, k, c, s):
    dp1 = do_solve(n, k, c, s)
    dp2 = do_solve(n, k, c, s[::-1])[::-1]

    res = []
    for i in range(n):
        if s[i] == 'x':
            continue
        l = dp1[i - 1] if i - 1 >= 0 else 0
        r = dp2[i + 1] if i + 1 < n else 0

        if l + r == k - 1:
            res.append(i + 1)
    return res


assert solve(16, 4, 3, 'ooxxoxoxxxoxoxxo') == [11, 16]
assert solve(11, 3, 2, 'ooxxxoxxxoo') == [6]
assert solve(5, 1, 0, 'ooooo') == []
assert solve(5, 2, 3, 'ooxoo') == [1, 5]

(n, k, c) = list(map(int, input().split()))
s = input().strip()

for num in solve(n, k, c, s):
    print(num)

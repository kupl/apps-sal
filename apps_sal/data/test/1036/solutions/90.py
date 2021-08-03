def winner(a, b):
    battle = {a, b}
    if battle == {'R', 'S'}:
        return 'R'
    elif battle == {'R', 'P'}:
        return 'P'
    elif battle == {'P', 'S'}:
        return 'S'
    return a


n, k = list(map(int, input().split()))
S = input()

# dp[2^k人のトーナメント][左端がSのi番目から始まるパターン] = 勝者の得意な手
dp = [[''] * n for _ in range(k + 1)]
for i in range(n):
    dp[0][i] = S[i]


def solve(k, i):
    if dp[k][i] == '':
        dp[k][i] = winner(solve(k - 1, i), solve(k - 1, (i + 2**(k - 1)) % n))
    return dp[k][i]


print(solve(k, 0))

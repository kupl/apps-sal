import copy

n = int(input())

mod = 10**9 + 7

memo = {}

banned = {'ACTG', 'TCAG', 'GCAG', 'TACG', 'AACG', 'ACAG', 'GAGC', 'CACG',
          'AGC', 'ATCG', 'ACCG', 'CAG', 'GACG', 'CCAG', 'AAGC', 'ACG', 'TAGC'}

count = 0


def dp(lettrs, state):

    if state in banned:
        return 0
    if lettrs == 0:
        return 1
    if (lettrs, state) in memo:
        return memo[lettrs, state]

    ans = 0
    for c in "ACGT":
        ans += dp(lettrs - 1, (state + c)[-4:])
        ans %= mod
    ans %= mod
    memo[lettrs, state] = ans

    return ans


print((dp(n, "")))

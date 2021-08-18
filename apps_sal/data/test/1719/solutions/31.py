
from collections import defaultdict

MOD = 10**9 + 7
N = int(input())
charactors = ['A', 'G', 'C', 'T']

dp = [defaultdict(int) for _ in range(N + 1)]

dp[0]['ZZZ'] = 1


def check(s, c):
    if c == 'C':
        if s[1:] == 'AG' or s[1:] == 'GA' or \
                (s[0] == 'A' and (s[1] == 'G' or s[2] == 'G')):
            return False
        else:
            return True
    elif c == 'G':
        if s[1:] == 'AC':
            return False
        else:
            return True
    else:
        return True


for i in range(N):
    for s in list(dp[i].keys()):
        for c in charactors:
            if check(s, c):
                dp[i + 1][s[1:] + c] += dp[i][s]
                dp[i + 1][s[1:] + c] %= MOD

print((sum(dp[N].values()) % MOD))

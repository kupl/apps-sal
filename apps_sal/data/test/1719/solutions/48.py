N = int(input())
mod = 10 ** 9 + 7
dp = [{} for i in range(N)]
forbid = set(['AGC', 'GAC', 'ACG'])


def search(i, prefix):
    if prefix in forbid:
        return 0
    elif i == N:
        return 1
    elif prefix in dp[i]:
        return dp[i][prefix]
    ret = 0
    for c in 'ACGT':
        if prefix[0] == 'A' and (prefix[1] == 'G' or prefix[2] == 'G') and (c == 'C'):
            continue
        ret += search(i + 1, prefix[1:] + c)
    dp[i][prefix] = ret % mod
    return ret % mod


print(search(0, 'BBB'))

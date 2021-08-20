from collections import defaultdict


def submit():
    n = int(input())
    modp = 10 ** 9 + 7
    chars = ['A', 'C', 'G', 'T']
    modp = 10 ** 9 + 7
    dp = [defaultdict(int) for _ in range(n + 1)]
    for c1 in chars:
        for c2 in chars:
            for c3 in chars:
                k = c1 + c2 + c3
                if k == 'AGC':
                    continue
                if k == 'ACG':
                    continue
                if k == 'GAC':
                    continue
                dp[3][k] = 1
    for i in range(4, n + 1):
        for (k, v) in dp[i - 1].items():
            for c in chars:
                if k[1] == 'A' and k[2] == 'G' and (c == 'C'):
                    continue
                if k[0] == 'A' and k[2] == 'G' and (c == 'C'):
                    continue
                if k[1] == 'G' and k[2] == 'A' and (c == 'C'):
                    continue
                if k[1] == 'A' and k[2] == 'C' and (c == 'G'):
                    continue
                if k[0] == 'A' and k[1] == 'G' and (c == 'C'):
                    continue
                new_k = k[1:] + c
                dp[i][new_k] += dp[i - 1][k]
                dp[i][new_k] %= modp
    ans = sum((v % modp for v in dp[n].values()))
    print(ans % modp)


submit()

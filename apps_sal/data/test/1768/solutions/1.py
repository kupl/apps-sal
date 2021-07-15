import sys

def solve():
    n = int(sys.stdin.readline().rstrip())
    s = sys.stdin.readline().rstrip()
    q = int(sys.stdin.readline().rstrip())

    pfs = [[0]*(n + 1) for i in range(26)]
    for i in range(n):
        ch = ord(s[i]) - ord('a')

        for j in range(26):
            if j == ch:
                pfs[j][i + 1] = pfs[j][i] + 1
            else:
                pfs[j][i + 1] = pfs[j][i]

    '''
    for i in range(26):
        print(chr(i + ord('a')), *pfs[i])
    print()
    '''

    dp = [[0]*(n + 1) for i in range(26)]

    for c in range(26):
        for l in range(n + 1):
            for r in range(l, n + 1):
                tc = r - l - (pfs[c][r] - pfs[c][l])
                dp[c][tc] = max(dp[c][tc], r - l)

        for i in range(1, n + 1):
            dp[c][i] = max(dp[c][i], dp[c][i - 1])

    '''
    for i in range(26):
        print(chr(i + ord('a')), *dp[i])
    '''

    for qi in range(q):
        mi, ci = sys.stdin.readline().split()
        mi = int(mi)
        ci = ord(ci) - ord('a')
        ans = dp[ci][mi]
        print(ans)

def __starting_point():
    solve()
__starting_point()

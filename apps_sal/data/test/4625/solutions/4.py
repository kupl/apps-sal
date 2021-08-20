ans = []
empt = [0 for i in range(26)]
s = 'abcdefghijklmnopqrstuvwxyz'
pos = {s[i]: i for i in range(26)}
for t in range(int(input())):
    [n, m] = [int(i) for i in input().split()]
    seq = input()
    err = [int(i) - 1 for i in input().split()]
    freq = {}
    for i in err:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    dp = [0 for i in range(n)]
    dp[n - 1] = 1
    for i in range(n - 2, -1, -1):
        dp[i] = dp[i + 1]
        if i in freq:
            dp[i] += freq[i]
    a = empt + []
    for i in range(n):
        a[pos[seq[i]]] += dp[i]
    ans.append(' '.join([str(i) for i in a]))
print('\n'.join(ans))

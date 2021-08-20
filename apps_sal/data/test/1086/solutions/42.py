(h, w) = map(int, input().split())
a = [list(map(int, input().split())) for i in range(h)]
b = [list(map(int, input().split())) for i in range(h)]
pos = 160 * 80
dp = [[0] * w for i in range(h)]
sub = abs(a[0][0] - b[0][0])
dp[0][0] = 1 << pos - sub | 1 << pos + sub
for c in range(h):
    for l in range(w):
        sub = abs(a[c][l] - b[c][l])
        if l != 0 and c != 0:
            dp[c][l] |= dp[c][l - 1] << sub | dp[c][l - 1] >> sub | dp[c - 1][l] << sub | dp[c - 1][l] >> sub
        elif c != 0:
            dp[c][l] |= dp[c - 1][l] << sub | dp[c - 1][l] >> sub
        elif l != 0:
            dp[c][l] |= dp[c][l - 1] << sub | dp[c][l - 1] >> sub
bit = dp[-1][-1]
for i in range(pos):
    if bit & 1 << pos + i or bit & 1 << pos - i:
        print(i)
        break

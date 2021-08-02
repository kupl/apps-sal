n = int(input())
s = input()
dp = [[-1] * (n + 1) for x in range(26)]

for c in range(26):
    for l in range(n):
        n_c = 0
        for r in range(l, n):
            if s[r] == chr(ord('a') + c):
                n_c += 1
            dp[c][r - l + 1 - n_c] = max(dp[c][r - l + 1 - n_c], r - l + 1)

all_res = []
for i in range(int(input())):
    m, c = input().split()
    m = int(m)
    idx = ord(c) - ord('a')
    all_res.append(dp[idx][m] if dp[idx][m] != -1 else n)

print('\n'.join(map(str, all_res)))

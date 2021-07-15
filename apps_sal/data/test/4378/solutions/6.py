n = int(input())
s = '!' + input().strip()

dp = [[10 ** 6] * (n + 1) for i in range(3)]
pr = [[None] * (n + 1) for i in range(3)]
dp[0][0] = dp[1][0] = dp[2][0] = 0
for i in range(1, n + 1):
    for c in range(3):
        op1 = dp[(c + 1) % 3][i - 1]
        op2 = dp[(c + 2) % 3][i - 1]
        pr[c][i] = (c + 1) % 3 if op1 < op2 else (c + 2) % 3
        dp[c][i] = min(op1, op2) + ('RGB'.index(s[i]) != c)

ans = []
end = [dp[0][n], dp[1][n], dp[2][n]]
c = end.index(min(end))
for i in range(n, 0, -1):
    ans.append(c)
    c = pr[c][i]

print(min(end))
print(''.join('RGB'[c] for c in ans[::-1]))

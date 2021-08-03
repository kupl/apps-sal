__author__ = 'Utena'
s = input()
n = len(s)
ans = set()
if n <= 6:
    print(0)
    return
dp = [[False, False]for i in range(n + 1)]
if n > 7:
    dp[3][1] = True
    ans.add(s[-3:])
dp[2][0] = True
ans.add(s[-2:])

for i in range(4, n - 4):
    if s[(-i):(-i + 2)] != s[(-i + 2):(-i + 3)] + s[-i + 3] and dp[i - 2][0] or dp[i - 2][1]:
        dp[i][0] = True
        ans |= {s[(-i):(-i + 2)]}
    if i >= 6 and s[(-i):(-i + 3)] != s[(-i + 3):(-i + 5)] + s[-i + 5] and dp[i - 3][1] or dp[i - 3][0]:
        dp[i][1] = True
        ans.add(s[(-i):(-i + 3)])
ans = sorted(list(ans))
print(len(ans))
print('\n'.join(ans))

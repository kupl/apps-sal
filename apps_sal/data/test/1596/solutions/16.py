u = list(input())
q = int(1e9) + 7
n = len(u)
if 'm' in u or 'w' in u:
    print(0)
    return
if n == 1:
    print(1)
    return
dp = [0] * n
dp[0] = 1
dp[1] = 2
for i in range(2, n):
    dp[i] = dp[i - 1] + dp[i - 2]
    dp[i] %= q
ans = 1
w = 0
m = 0
#print(dp)
if u[0] == 'u':
    w += 1
elif u[0] == 'n':
    m += 1
for i in range(1, n):
    if u[i] == 'u':
        w += 1
    elif u[i] == 'n':
        m += 1
    if u[i] != 'u' and w != 0:
        ans *= dp[w - 1]
        w = 0
    if u[i] != 'n' and m != 0:
        ans *= dp[m - 1]
        m = 0
    ans %= q
if w != 0:
    ans *= dp[w - 1]
if m != 0:
    ans *= dp[m - 1]
print(ans % q)










    


MOD = 10**9 + 7

s = input()
n = len(s)

if s.count('m') > 0 or s.count('w') > 0:
    print('0')
    return

us, ns = [0], [0]
dp = [1 for i in range(n + 1)]
for i in range(2, n + 1):
    dp[i] = (dp[i - 1] + dp[i - 2]) % MOD

for i in range(n):
    if s[i] == 'u':
        us[-1] += 1
        ns.append(0)
    elif s[i] == 'w':
        us[-1] += 2
        ns.append(0)
    elif s[i] == 'n':
        ns[-1] += 1
        us.append(0)
    elif s[i] == 'm':
        ns[-1] += 2
        us.append(0)
    else:
        us.append(0)
        ns.append(0)
#print(us, ns)
ans = 1
for usi in us:
    ans = (ans * dp[usi]) % MOD
for nsi in ns:
    ans = (ans * dp[nsi]) % MOD
print(ans)

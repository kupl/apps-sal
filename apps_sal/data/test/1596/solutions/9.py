"""T=int(input())
for _ in range(0,T):
    N=int(input())
    a,b=map(int,input().split())
    s=input()
    s=[int(x) for x in input().split()]
    for i in range(0,len(s)):
        a,b=map(int,input().split())"""


MOD = 1000000007
s = input()
flag = 0
for i in range(0, len(s)):
    if(s[i] == 'w' or s[i] == 'm'):
        flag = 1
        break

if(flag == 0):
    c = 1
    g = []
    for i in range(1, len(s)):
        if(s[i] == s[i - 1]):
            c = (c + 1) % MOD
        else:
            if(s[i - 1] == 'n' or s[i - 1] == 'u'):
                g.append(c)
            c = 1

    if(s[-1] == 'n' or s[-1] == 'u'):
        g.append(c)
    dp = [0, 1, 2, 3]
    ggg = 10
    if(len(g) > 0):
        ggg = max(g) + 10
    else:
        ggg = 10
    for i in range(ggg):
        dp.append((dp[-1] + dp[-2]) % MOD)

    ans = 1
    for i in range(0, len(g)):
        ans = (ans * (dp[g[i] % MOD]) % MOD) % MOD

    print(ans % MOD)
else:
    print(0)

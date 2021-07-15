import sys
readline = sys.stdin.readline

MOD = 10**9+7
N, M = list(map(int, readline().split()))
S = list(map(int, readline().strip()))
Query = [tuple([int(x) - 1 for x in readline().split()]) for _ in range(M)]

PP = S.count(1)

Li = [None]*PP
Ri = [None]*PP

T1 = S[:]
for l, r in Query:
    cnt = 0
    for i in range(l, r+1):
        cnt += T1[i]
    for i in range(l, l+cnt):
        T1[i] = 1
    for i in range(l+cnt, r+1):
        T1[i] = 0
T2 = S[:]
for l, r in Query:
    cnt = 0
    for i in range(l, r+1):
        cnt += 1 - T2[i]
    for i in range(l, l+cnt):
        T2[i] = 0
    for i in range(l+cnt, r+1):
        T2[i] = 1

cnt = 0
for i in range(N):
    if T1[i]:
        Li[cnt] = i
        cnt += 1
cnt = 0
for i in range(N):
    if T2[i]:
        Ri[cnt] = i+1
        cnt += 1

dp = [0]*N
for i in range(Li[0], Ri[0]):
    dp[i] = 1

for j in range(1, PP):
    dp2 = [0] + dp[:-1]
    for i in range(1, N):
        dp2[i] = (dp2[i]+dp2[i-1])%MOD
    for i in range(Li[j]):
        dp2[i] = 0
    for i in range(Ri[j], N):
        dp2[i] = 0
    dp = dp2[:]
res = 0
for d in dp:
    res = (res+d)%MOD
print(res)
    


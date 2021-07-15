import sys
input = sys.stdin.readline

n,m = map(int,input().split())
dg = 10**10

s = [0]
t = [0]

tank = []
for _ in [0]*n:
    X,d = map(int,input().split())
    tank.append((X+d)*dg + X)
tank.sort()

for e in tank:
    X_d = e//dg
    X = e%dg
    d = X_d-X
    s.append(max(1,X_d-d*2))
    t.append(min(m,X_d))


n += 1

dp = [[0]*(m+1) for i in range(2)]
for j in range(1,t[0]+1):
    dp[0][j] = s[0]-1
for j in range(t[0]+1,m+1):
    dp[0][j] = max(s[0]-1,j-t[0])

for i in range(1,n):
    for j in range(1,m+1):
        tmp = dp[(i+1)%2][j]
        if j <= t[i]:
            tmp = min(tmp,dp[(i+1)%2][s[i]-1])
        else:
            tmp = min(tmp,dp[(i+1)%2][max(0,s[i]+t[i]-j-1)]+j-t[i])
        dp[i%2][j] = tmp

print(dp[(n+1)%2][-1])

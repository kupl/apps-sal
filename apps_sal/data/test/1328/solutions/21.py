n,ma,mb = list(map(int,input().split()))
l = []
sum_a = 0
sum_b = 0
for _ in range(n):
    a,b,c = list(map(int,input().split()))
    sum_a += a
    sum_b += b
    l.append([a,b,c])

INF = 10**10
dp = list( list([INF for i in range(450)] for i in range(450)) for i in range(45))
dp[0][0][0] = 0
for i in range(n):
    for s in range(sum_a+1):
        for k in range(sum_b+1):
            a,b,c = l[i]
            dp[i+1][s][k] = min(dp[i][s][k], dp[i+1][s][k],dp[i][s-a][k-b]+c)

ans = 10**10
k = 1
while ma*k < 450 and mb*k < 450 :
    ans = min(ans, dp[n][ma*k][mb*k])
    k += 1
if ans != 10**10:
  print(ans)
else:
  print((-1))


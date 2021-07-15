n, k = map(int,input().split())
dp = [0]
bound = [0]
a = list(map(int,input().split()))

for i in range(1, n+1):
    dp.append(dp[a[i-1]])
    bound.append(i+k)
    t1 = max(bound[a[i-1]]+1, i-k)
    t2 = min(i+k, n)
    t3 = t2 - t1 + 1
    if t3>0: dp[i] += t3

for i in range(1, n+1):
    print(dp[i],end = ' ')


"""
from
http://codeforces.com/contest/811/problem/C
"""
length = int(input())
array = [0] + [int(x) for x in input().split()]
dp = [0]*(length+1)
end = [0]*5001
start = [5001]*5001
vis = [0]*5001

for i in range(1,length+1):
    start[array[i]] = min(start[array[i]],i)
    end[array[i]] = max(end[array[i]],i)

for i in range(1, length + 1):
    dp[i] = dp[i-1]
    chk = [0] * 5001
    ll = i
    cur = 0
    for j in range(i,0,-1):
        ll = min(ll,start[array[j]])
        if end[array[j]] > i:break
        if chk[array[j]] == 0:
            cur = array[j] ^ cur
            chk[array[j]] = 1
        if ll == j:
            dp[i] = max(dp[i],dp[j-1]+cur)
print(dp[length])

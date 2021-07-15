from sys import stdin
n=int(stdin.readline().strip())
dp=[0 for i in range(6)]
d={4: 0, 8: 1, 15: 2, 16: 3, 23: 4, 42: 5}
s=list(map(int,stdin.readline().strip().split()))
for i in range(n-1,-1,-1):
    if s[i]==42:
        dp[5]+=1
        continue
    elif dp[d[s[i]]+1]>dp[d[s[i]]]:
        dp[d[s[i]]]+=1
print(n-6*dp[0])


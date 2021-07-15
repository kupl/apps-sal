n, q = list(map(int, input().split()))
s = input()

dp = [0]*n
temp = 0
for i in range(1,n):
    if s[i-1]=="A" and s[i] =="C":
        temp +=1
    dp[i] =temp

for i in range(q):
    l, r = list(map(int, input().split()))
    print((dp[r-1]-dp[l-1]))


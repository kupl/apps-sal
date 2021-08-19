"""
n=int(input())
s=[int(x) for x in input().split()]+[n]
pos=[]
for i in range(0,len(s)-1):
    temp=-1
    p=i+1
    for j in range(i+1,s[i]):
        if(temp<s[j]):
            temp=max(temp,s[j])
            p=j
    pos.append(p)

pos.append(0)

ans=0
dp=[0]*n
for i in range(n-2,-1,-1):
    dp[i]=(n-i)+(dp[pos[i]])-(s[i]-pos[i])
    ans+=dp[i]

#print(s)
#print(pos)
#print(dp)
print(ans)



"""

import math
n = int(input())
s = [int(x) for x in input().split()] + [n]


K = int(math.log2(n)) + 1
lookup = []
for i in range(n + 1):
    h = []
    for j in range(K + 1):
        h.append(0)
    lookup.append(h)


for i in range(0, n):
    lookup[i][0] = (s[i], i)

for j in range(1, K + 1):
    # j=1
    # while((1<<j)<=n):
    i = 0
    while(i + (1 << j) - 1 < n):
        if(lookup[i][j - 1][0] > lookup[i + (1 << (j - 1))][j - 1][0]):
            lookup[i][j] = (lookup[i][j - 1][0], lookup[i][j - 1][1])
        else:
            lookup[i][j] = (lookup[i + (1 << (j - 1))][j - 1][0], lookup[i + (1 << (j - 1))][j - 1][1])
        i += 1
    j += 1


pos = []
for i in range(0, len(s) - 1):
    L = i + 1
    R = s[i] - 1
    j = int(math.log2(R - L + 1))
    if(lookup[L][j][0] > lookup[R - (1 << j) + 1][j][0]):
        pos.append(lookup[L][j][1])
    else:
        pos.append(lookup[R - (1 << j) + 1][j][1])


ans = 0
dp = [0] * n
for i in range(n - 2, -1, -1):
    dp[i] = (n - i) + (dp[pos[i]]) - (s[i] - pos[i])
    ans += dp[i]

print(ans)

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
    pos.append(j)

pos.append(0)

ans=0
dp=[0]*n
for i in range(n-2,-1,-1):
    dp[i]=(n-i-1)+(dp[pos[i]])-(s[i]-pos[i]-1)
    ans+=dp[i]
print(pos)
print(dp)
print(ans)
"""
import math
'\nn=int(input())\ns=[1]+[int(x) for x in input().split()]+[n]\npos=[0]\nfor i in range(1,len(s)-1):\n    temp=-1\n    p=i+1\n    for j in range(i+1,s[i]+1):\n        if(temp<s[j]):\n            temp=max(temp,s[j])\n            p=j\n    pos.append(p)\n\npos.append(0)\n\nans=0\ndp=[0]*(n+1)\nfor i in range(n-1,0,-1):\n    dp[i]=(n-i)+(dp[pos[i]])-(s[i]-pos[i])\n    ans+=dp[i]\n\n#print(s)\n#print(pos)\n#print(dp)\nprint(ans)\n\n\n\nn=int(input())\ns=[int(x) for x in input().split()]+[n]\npos=[]\nfor i in range(0,len(s)-1):\n    temp=-1\n    p=i+1\n    for j in range(i+1,s[i]):\n        if(temp<s[j]):\n            temp=max(temp,s[j])\n            p=j\n    pos.append(p)\n\npos.append(0)\n\nans=0\ndp=[0]*n\nfor i in range(n-2,-1,-1):\n    dp[i]=(n-i)+(dp[pos[i]])-(s[i]-pos[i])\n    ans+=dp[i]\n\n#print(s)\n#print(pos)\n#print(dp)\nprint(ans)\n\n\n\n'
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
    i = 0
    while i + (1 << j) - 1 < n:
        if lookup[i][j - 1][0] > lookup[i + (1 << j - 1)][j - 1][0]:
            lookup[i][j] = (lookup[i][j - 1][0], lookup[i][j - 1][1])
        else:
            lookup[i][j] = (lookup[i + (1 << j - 1)][j - 1][0], lookup[i + (1 << j - 1)][j - 1][1])
        i += 1
    j += 1
'pos=[]\nfor i in range(0,len(s)-1):\n    temp=-1\n    p=i+1\n    for j in range(i+1,s[i]):\n        if(temp<s[j]):\n            temp=max(temp,s[j])\n            p=j\n    pos.append(p)\n\npos.append(0)'
pos = []
for i in range(0, len(s) - 1):
    L = i + 1
    R = s[i] - 1
    j = int(math.log2(R - L + 1))
    if lookup[L][j][0] > lookup[R - (1 << j) + 1][j][0]:
        pos.append(lookup[L][j][1])
    else:
        pos.append(lookup[R - (1 << j) + 1][j][1])
ans = 0
dp = [0] * n
for i in range(n - 2, -1, -1):
    dp[i] = n - i + dp[pos[i]] - (s[i] - pos[i])
    ans += dp[i]
print(ans)

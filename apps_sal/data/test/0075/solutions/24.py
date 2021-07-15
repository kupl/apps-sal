import sys, math, string, fractions, functools, collections
sys.setrecursionlimit(10**7)
RI=lambda x=' ': list(map(int,input().rstrip().split(x)))
RS=lambda x=' ': input().rstrip().split(x)
dX= [-1, 1, 0, 0,-1, 1,-1, 1]
dY= [ 0, 0,-1, 1, 1,-1,-1, 1]
mod=int(1e9+7)
eps=1e-6
MAX=1010
#################################################
col=[0]*MAX
row=[0]*MAX
tot=0
n, m = RI()
s=[0]*MAX
for i in range(n):
    s[i]=RS()[0]
    for j in range(m):
        if s[i][j]=='*':
            row[i]+=1
            col[j]+=1
            tot+=1
for i in range(n):
    for j in range(m):
        if row[i]+col[j]- (s[i][j]=='*')==tot:
            print("YES")
            print(i+1, j+1)
            return
print("NO")

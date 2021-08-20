"""n,L,a=map(int,input().split())
#s=[int(x) for x in input().split()]
ed=0
ct=0
for j in range(0,n):
    t,l=map(int,input().split())
    ct=ct+((t-ed)//a)
    ed=t+l
t=L
ct=ct+((t-ed)//a)
print(ct)"""
import math
"n,m=map(int,input().split())\ndp=[[-1 for i in range(m)] for j in range(n)]\ndp2=[[-1 for i in range(m)] for j in range(n)]\n#dp=[]\n#dp2=[]\nfor i in range(0,n):\n    s=input()\n    for j in range(0,m):\n        if(s[j]=='.'):\n            dp[i][j]=-1\n        else:\n            dp[i][j]=s[j]\nfor i in range(0,n-2):\n    for j in range(0,m-2):\n        #print(i,j)\n        p=0\n        c=0\n        for k in range(i,i+3):\n            for h in range(j,j+3):\n                p=p+1\n                if(p!=5):\n                    if(dp[k][h]=='#'):\n                        c=c+1\n\n                    \n        if(c==8):\n            p=0\n            for k in range(i,i+3):\n                for h in range(j,j+3):7\n                    p=p+1\n                    if(p!=5):\n                        dp2[k][h]='#'\n\n\n                        \n#print(dp)\n#print(dp2)\nif(dp==dp2):\n    print('YES')\nelse:\n    print('NO')"
n = int(input())
if n == 3:
    print('1 1 3')
else:
    t = 1
    while t <= n:
        ct = math.ceil(n // t / 2)
        for i in range(0, ct):
            print(t, end=' ')
        if ct == 2 and n // t % 2 != 0:
            t = t * 3
        else:
            t = t * 2
    print(' ')

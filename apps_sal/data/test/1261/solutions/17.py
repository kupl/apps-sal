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

"""n,m=map(int,input().split())
dp=[[-1 for i in range(m)] for j in range(n)]
dp2=[[-1 for i in range(m)] for j in range(n)]
#dp=[]
#dp2=[]
for i in range(0,n):
    s=input()
    for j in range(0,m):
        if(s[j]=='.'):
            dp[i][j]=-1
        else:
            dp[i][j]=s[j]
for i in range(0,n-2):
    for j in range(0,m-2):
        #print(i,j)
        p=0
        c=0
        for k in range(i,i+3):
            for h in range(j,j+3):
                p=p+1
                if(p!=5):
                    if(dp[k][h]=='#'):
                        c=c+1

                    
        if(c==8):
            p=0
            for k in range(i,i+3):
                for h in range(j,j+3):7
                    p=p+1
                    if(p!=5):
                        dp2[k][h]='#'


                        
#print(dp)
#print(dp2)
if(dp==dp2):
    print('YES')
else:
    print('NO')"""


import math
n=int(input())
if(n==3):
    print('1 1 3')

else:
    t=1
    while(t<=n):
        ct=math.ceil((n//t)/2)
        for i in range(0,ct):
            print(t,end=" ")
        #t=t*2
        if(ct==2 and (n//t)%2!=0):
            t=t*3
        else:
            t=t*2
    print(" ")

                            


icase=0
if icase==0:
    h,w=list(map(int,input().split()))
    dp=[[0]*10 for i in range(10)]
    for i in range(10):
        dp[i]=list(map(int,input().split()))
    a=[]
    for i in range(h):
        a.extend(list(map(int,input().split())))
elif icase==1:
    h,w=2,4
    dp=[[0, 9, 9, 9, 9, 9, 9, 9, 9, 9], 
       [9, 0, 9, 9, 9, 9, 9, 9, 9, 9],
       [9, 9, 0, 9, 9, 9, 9, 9, 9, 9],
       [9, 9, 9, 0, 9, 9, 9, 9, 9, 9],
       [9, 9, 9, 9, 0, 9, 9, 9, 9, 2],
       [9, 9, 9, 9, 9, 0, 9, 9, 9, 9],
       [9, 9, 9, 9, 9, 9, 0, 9, 9, 9],
       [9, 9, 9, 9, 9, 9, 9, 0, 9, 9],
       [9, 9, 9, 9, 2, 9, 9, 9, 0, 9],
       [9, 2, 9, 9, 9, 9, 9, 9, 9, 0]]

    a=[-1, -1, -1, -1, 8, 1, 1, 8]

from collections import Counter
ac=Counter(a)

n=10
for k in range(n):
    for i in range(n):
        for j in range(n):
            dp[i][j]=min(dp[i][j],dp[i][k]+dp[k][j])

icnt=0
for i in range(10):
    if ac[i]>0:
        icnt+=dp[i][1]*ac[i]  

print(icnt)      


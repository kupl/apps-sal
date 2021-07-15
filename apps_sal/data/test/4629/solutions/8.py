coins=[3**i for i in range(26)]
t=(1<<12)
sm=[]
for i in range(t):
    c=0 
    for j in range(12):
        if i&(1<<j):
            c+=coins[j]
    sm.append(c)
sm.sort() 
from bisect import bisect_left as bl 
for _ in range(int(input())):
    n=int(input())
    ind=bl(sm,n)
    print(sm[ind])
    


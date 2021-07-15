# cook your dish here
# from math import * 
for _ in range(int(input().strip())):
    n=int(input())
    t=1 
    l=[]
    for __ in range(n):
        l.append(list(map(int,input().split())))
    i=0
    ans=[]
    t=1
    while t<=5002:
        if l[i][0]>t:
            t+=1
            continue
        if l[i][0]<=t and l[i][1]>=t:
            ans.append(t)
            t+=1
            i+=1 
        else:
            ans.append(0)
            i+=1
        if i==n:
            break
    print(*ans)        
        


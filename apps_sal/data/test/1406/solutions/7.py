m=list(input().split())
n=int(m[0])
k=int(m[1])
d=int(m[2])

if n==1:
    for i in range(d):
        print("1")
    return
if k==1:
    print("-1")
    return
if k>=n:
    m=list(i for i in range(n))
    o=""
    for j in range(1,n+1):
        o+=" "+str(j)
    o=o[1:] 
    for i in range(d):
        print(o)
    return
if d==1:
    print('-1')
    return
if d>=n:
    m=list("1" for i in range(n))
    for i in range(n):
        m[i]="2"
        #print(m)
        o=str(m[0])
        for j in range(1,n):
            o+=" "+str(m[j])
        print(o)
        #m[i]="1"
    for i in range(n,d):
        #print(m)
        print(o)
    return

from math import ceil, floor
tc=ceil(n/k) #days
tf=floor(n/k) #len k

if n>(k**d):
    print('-1')
    return

sc=1
for stp in range(1,d+1):
    o=""
    kc=0
    
    while kc<n:
        for kk in range(1,k+1):
            for i in range (sc):
                if kc<n:
                    o+=' '+str(kk)
                    kc+=1
                else:
                    break
    sc*=k #change from 2
    print(o[1:])


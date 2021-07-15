t=int(input())
for you in range(t):
    l=input().split()
    n=int(l[0])
    x=int(l[1])
    l=input().split()
    li=[int(i) for i in l]
    poss=1
    for i in li:
        if(i!=x):
            poss=0
            break
    if(poss):
        print(0)
        continue
    poss=0
    for i in li:
        if(i==x):
            poss=1
            break
    if(poss):
        print(1)
        continue
    z=sum(li)
    if(z==n*x):
        print(1)
        continue
    print(2) 


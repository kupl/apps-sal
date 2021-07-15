t=int(input())
while t>0:
    t-=1
    n=int(input())
    a=[int(x) for x in input().split()]
    m=int(input())
    b=[int(x) for x in input().split()]
    e1=o1=e2=o2=0
    for i in a:
        if i%2==0:
            e1+=1
        else:
            o1+=1
    for i in b:
        if i%2==0:
            e2+=1
        else:
            o2+=1  
    s=e1*e2+o1*o2
    print(s)

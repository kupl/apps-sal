__author__ = 'Utena'
n=input().split()
if n[2]=='week':
    n=int(n[0])
    if n==5 or n==6:
        print(53)
    else:print(52)
else:
    n=int(n[0])
    total=0
    for i in range(1,13):
        if i in (1,3,5,7,8,10,12):
            total+=1
        elif i in(4,6,9,11):
            if n<=30:total+=1
        else:
            if n<=29:total+=1
    print(total)

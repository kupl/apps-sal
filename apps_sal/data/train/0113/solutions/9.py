for i in ' '*int(input()):
    a,b=map(int,input().split())
    k=abs(b-a)
    c=0
    c+=k//5
    k%=5
    if k>3:
        c+=1
        k=5-k
    c+=k//2
    k%=2
    c+=k
    print(c)

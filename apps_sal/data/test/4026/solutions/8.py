for i in ' '*int(input()):
    n,m=map(int,input().split())
    L=[]
    state=False
    for i in ' '*n:
        a,b=map(int,input().split())
        c,d=map(int,input().split())
        if b==c:state=True
    if m%2:state=False
    print(['NO','YES'][state])

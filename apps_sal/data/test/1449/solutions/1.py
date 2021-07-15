y=lambda:[*map(int,input().split())]
for _ in range(int(input())):
    n,k=map(int,input().split())
    a=y()
    b=len(set(a))
    if k<2:print(1-2*(b>1))
    else:print(max(1,-((1-b)//(k-1))))

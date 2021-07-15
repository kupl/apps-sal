X,Y=list(map(int,input().split()))

if X+Y<=1:
    print("Brown")

else:
    n=X-Y
    if n<0:
        n=(-1)*n
    
    if n<=1:
        print("Brown")
    else:
        print("Alice")


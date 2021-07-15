T=int(input())
while T>0:
    T-=1
    n,l,r=list(map(int,input().split()))
    t = n//l
    if t*r>=n:
        print("Yes")
    else:
        print("No")


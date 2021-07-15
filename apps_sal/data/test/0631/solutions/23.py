t=int(input())
for i in range(t):
    n,m=list(map(int,input().split()))
    b=list(map(int,input().split()))
    if sum(b)==m:
        print("YES")
    else:
        print("NO")


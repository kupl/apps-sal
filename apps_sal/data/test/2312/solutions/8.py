t=int(input())
for i in range(t):
    n=int(input())
    b=list(map(int,input().split()))
    if len(set(b))==n:
        print("NO")
    else:
        print("YES")



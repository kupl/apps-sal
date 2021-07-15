t=int(input())
for q in range(t):
    n,k1,k2=map(int,input().split())
    a1=max(list(map(int,input().split())))
    a2=max(list(map(int,input().split())))
    if a1>a2:
        print("YES")
    else:
        print("NO")

n=int(input())
prev=max(list(map(int,input().split())))
for i in range(n-1):
    a,b=list(map(int,input().split()))
    if max(a,b)<=prev:
        prev=max(a,b)
    elif min(a,b) <= prev:
        prev=min(a,b)
    else:
        print("NO")
        break
else:
    print("YES")


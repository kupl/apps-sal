q=int(input())
for i in range(q):
    n,k=[int(x) for x in input().split()]
    a=[int(x) for x in input().split()]
    x=min(a)
    y=max(a)
    if x+k<y-k:
        print(-1)
    else:
        print(x+k)


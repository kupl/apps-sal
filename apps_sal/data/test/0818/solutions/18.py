n=int(input())

if n<3:
    print(-1)
else:
    k=int(pow(10,n-1))
    l=k+210-(k%210)
    print(l)


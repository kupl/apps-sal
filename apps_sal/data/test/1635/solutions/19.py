def ma():
    n=int(input())
    b=list(map(int,input().split()))
    k={b[-1]};last=b[-1]
    for i in range(n-1,-1,-1):
        if not (b[i] in k):
            last=b[i];
            k.add(b[i])
    print(last)
ma()

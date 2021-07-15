t=int(input())
for _ in range(t):
    n,k=list(map(int,input().split()))
    if n%2==0:
        print(n+2*k)
    else:
        i=2
        while 1>0:
            if n%i==0:
                break
            i=i+1
        n=n+i
        k=k-1
        print(n+2*k)

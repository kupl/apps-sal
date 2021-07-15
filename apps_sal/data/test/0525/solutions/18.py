t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    same=1
    for i in range(n-1):
        if a[i]!=a[i+1]:
            same=0
            break
    if same==1:
        print(n)
    else:
        print(1)

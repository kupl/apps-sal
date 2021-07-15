n=int(input())
for i in range(n):
    a=list(map(int,input().split()))
    if a[1]!=a[3]:
        print(a[1],a[3])
    else:
        print(a[1]-1,a[3])

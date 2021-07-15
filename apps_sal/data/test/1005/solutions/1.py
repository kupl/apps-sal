t=int(input())
for p in range(t):
    n,k,d=[int(x) for x in input().split()]
    a=[int(x) for x in input().split()]
    arr=10**100
    for i in range(0,n-d+1):
        b=set()
        for j in range(i,i+d):
            b.add(a[j])
        arr=min(arr,len(b))
        b=set()
    print(arr)


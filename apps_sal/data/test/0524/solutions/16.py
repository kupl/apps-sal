n=int(input())
arr=list(map(int,input().split()))
arr.sort()
m=0
for i in arr:
    m+=abs(i-1)
c=2
if n>10:
    while c<20:
        t=0
        for i in range(n):
            t+=abs(c**i-arr[i])
            if t>=m:
                break
        if t<m:
            m=t
        c+=1
    print(m)
else:
    while c<=1000000:
        t=0
        for i in range(n):
            t+=abs(c**i-arr[i])
            if t>=m:
                break
        if t<m:
            m=t
        c+=1
    print(m)


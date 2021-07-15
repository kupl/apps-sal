n=int(input())

a=list(map(int, input().split()))

s0=sum(a)
if s0%3!=0:
    print(0)
else:
    s=s0//3
    d=[0 for i in range(n)]
    temp=a[-1]
    d[-1]= 1 if temp==s else 0
    for i in range(2, n+1):
        temp+=a[-i]
        d[-i]=d[-i+1] + (1 if temp==s else 0)
    k=0
    temp=0
    for i in range(n-2):
        temp+=a[i]
        if temp==s:
            k+=d[i+2]
    print(k)


N=int(input())
a=list(map(int, input().split()))

while 1:
    temp=[]
    a.sort()
    k=a[0]
    f=0
    for i in range(1,len(a)):
        if a[i]%k!=0:
            f=1
            temp.append(a[i]%k)
    if temp==[] or f==0:
        print(k)
        return
    a=[k]+temp

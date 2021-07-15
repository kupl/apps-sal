T=int(input())
while(T>0):
    n=int(input())
    p=[(int(i)-1) for i in input().split()]
    #print(p)
    ans=[]
    for i in range(0,n):
        curr=i
        count=1
        next=p[curr]
        while(next!=curr):
            next=p[next]
            count+=1
        ans.append(count)
    for i in range(0,len(ans)):
        print(ans[i],end=' ')
    print()
    T-=1

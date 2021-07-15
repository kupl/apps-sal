for _ in range(int(input())):
    n,x=map(int,input().split())
    s=input()
    y=s.count('0')-s.count('1')
    z=0
    inf=False
    ans=0
    if x==0: ans=1
    for i in s:
        z+=(i=='0')-(i=='1')
        if y==0 and z==x:
            inf=True
            print(-1)
            break
        if x-z==0 or ((x-z)*y>0 and (x-z)%y==0):ans+=1
    if not inf:
        print(ans)

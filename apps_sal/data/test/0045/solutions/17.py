def ma():
    s=input()
    nums=s.split(' ')
    n=int(nums[0])
    k=int(nums[1])
    base=k*(k+1)//2
    if n<base:
        print(-1)
        return 
    m=n//base
    if m*m<=n:
        while n%m!=0:
            m-=1
    else:
        p=(n-1)//m+1
        while p*p<=n and n%p!=0:
            p+=1
        if n%p==0:
            m=n//p
        else:
            q=(n-1)//m
            while n%q!=0:
                q-=1
            m=q
            
    for i in range(k-1):
        print(str((i+1)*m),end='')
        print(' ',end='')
    print(n-k*(k-1)//2*m)
ma()

N,A,R,M=map(int,input().split())
h=list(map(int,input().split()))
if A*R==0:
    print(0)
    return

if M>A+R:
    def condition(num):
        test=0
        for i in range(N):
            if num>h[i]:
                test+=A
            else:
                test-=R
        return 0>=test
    start=1
    end=10**10
    while end-start>1:
        test=(end+start)//2
        if condition(test):
            start=test
        else:
            end=test
    if condition(end):
        ans=0
        for i in range(N):
            if end>h[i]:
                ans+=A*(end-h[i])
            else:
                ans+=R*(h[i]-end)
        print(ans)
    elif condition(start):
        ans=0
        for i in range(N):
            if start>h[i]:
                ans+=A*(start-h[i])
            else:
                ans+=R*(h[i]-start)
        print(ans)
    else:
        print(R*sum(h))
else:
    H=sum(h)
    q=H//N
    #0~q弾で考え
    test1=0
    def condition1(num):
        count=0
        for i in range(N):
            count+=int((h[i]<num))
        return 0>=M*count-R*N

    start=1
    end=q
    while end-start>1:
        test=(end+start)//2
        if condition1(test):
            start=test
        else:
            end=test
    if condition1(end):
        for i in range(N):
            if end>h[i]:
                test1+=M*(end-h[i])
        test1+=R*(H-N*end)
    elif condition1(start):
        for i in range(N):
            if start>h[i]:
                test1+=M*(start-h[i])
        test1+=R*(H-N*start)
    else:
        test1=H*R

    #q+1~max(h)
    test2=0
    def condition2(num):
        count=0
        for i in range(N):
            count+=int((h[i]>num))
        return 0>=count*M-A*N
    start=q+1
    end=max(h)-1
    while end-start>1:
        test=(end+start)//2
        if condition2(test):
            end=test
        else:
            start=test
    if condition2(start):
        for i in range(N):
            if h[i]>=start:
                test2+=M*(h[i]-start)
        test2+=A*(N*start-H)
    elif condition2(end):
        for i in range(N):
            if h[i]>=end:
                test2+=M*(h[i]-end)
        test2+=A*(N*end-H)
    else:
        test2=A*(N*max(h)-H)
    print(min(test1,test2))

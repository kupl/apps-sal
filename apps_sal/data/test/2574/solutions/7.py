for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    a.sort()
    ans=0
    t1=a[0]*a[1]*a[2]*a[3]*a[-1]
    t2=a[0]*a[1]*a[-2]*a[-3]*a[-1]
    t3=a[-5]*a[-4]*a[-2]*a[-3]*a[-1]
    
    print(max(t1,t2,t3))

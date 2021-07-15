n=int(input())
if n%2==0:
    print(-1)
elif n==1:
    print(0)
    print(0)
    print(0)
else:
    p=[0]*n
    q=[0]*n
    w=[0]*n
    t=int(n/2)
    for i in range (0,n):
        p[i]=i
        if i<t:
            q[i]=n-2-2*i
        else:
            q[i]=4*t-2*i
        if i<=n-2:
            w[i]=n-2-i
        else:
            w[i]=n-1
    for i in range (0,n):
        if i!=n-1:
            print(p[i],end=' ')
        else:
            print(p[i])
    for i in range (0,n):
        if i!=n-1:
            print(q[i],end=' ')
        else:
            print(q[i])
    for i in range (0,n):
        if i!=n-1:
            print(w[i],end=' ')
        else:
            print(w[i])









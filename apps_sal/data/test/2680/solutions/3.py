def f(n,b):
    x=list(map(int,input().split()))
    y=list(map(int,input().split()))
    count = 0
    diff = [(1,n), (n,1), (n,n), (1,1)]
    for i in range(b):
        m=9999999
        for j in diff:
            a=abs(x[i]-j[0])+abs(y[i]-j[1])
            m=min(m,a)
        count += m
    return count
n,b=list(map(int,input().split()))
print(f(n,b))

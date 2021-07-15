I=lambda:map(int,input().split())
n,k=I();a=list(I());b=list(range(1,n*k+1))
for i in a:b.remove(i)
for i in range(k):
    print(' '.join(map(str,[a[i]]+b[i*(n-1):i*(n-1)+n-1])))

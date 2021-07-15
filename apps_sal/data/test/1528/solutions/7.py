n,x=map(int, input().split())
p=[1]*(n+1) #パティ
a=[1]*(n+1) #パティとバンズ

for i in range(1,n+1):
    p[i]=p[i-1]*2+1
    a[i]=a[i-1]*2+3

def f(n,x):
    if x==0:
        return 0
    if n==0:
        return 1
    
    center = a[n-1] + 2
    
    if x < center:
        return f(n-1,x-1)
    elif x >= center:
        return p[n-1] + 1 + f(n-1,x-center)

print(f(n,x))

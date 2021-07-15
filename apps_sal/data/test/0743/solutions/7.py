def nod(x,y):
    while x*y:
        if x>y:
            x%=y
        else:
            y%=x
    return x+y


n=int(input())
a=list(map(int,input().split()))
m=a[0]
for i in range(1,n):
    m=nod(m,a[i])
print(n*m)

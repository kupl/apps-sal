n=int(input())
if n%2==0:
    print(-1)
else:
    a=[]
    b=[]
    c=[]
    for i in range(n):
        a.append(i)
        if i==0:
            b.append(n-1)
        else:
            b.append(i-1)
        c.append((a[i]+b[i])%n)
    print(*a)
    print(*b)
    print(*c)

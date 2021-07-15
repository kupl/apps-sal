n=int(input())
a=list(map(str,input().split()))
b,c=[],[]
if n%2==0:
    for i in range(n):
        if i%2==0:
            b.append(a[i])
        else:
            c.append(a[i])
    c.reverse()
else:
    for i in range(n):
        if i%2==1:
            b.append(a[i])
        else:
            c.append(a[i])
    c.reverse()
print(" ".join(c+b))

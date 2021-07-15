a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
f=int(input())
if e>=f:
    ans=e*min(a,d)
    k=min(a,d)
    a -= k
    d -= k
    ans += f*min(b,c,d)
    print(ans)
else:
    ans=f*min(b,c,d)
    k=min(b,c,d)
    b -= k
    c -= k
    d -= k
    ans += e*min(a,d)
    print(ans)

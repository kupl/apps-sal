x,k,d=map(int,input().split())
q=abs(x)//d
if q>=k:
    print(abs(x)-k*d)
else:
    now=abs(x)-q*d
    r=k-q
    if r%2==0:
        print(now)
    else:
        print(d-now)

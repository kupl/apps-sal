a,b=tuple(map(int,input().strip().split()))
if(a==b):
    print(0)
else:
    if(a>b):
        c=a-b
    else:
        c=b-a
    import math
    i=math.ceil(math.sqrt(c))
    l=[]
    for k in range(1,i):
        if(c%k==0):
            l.append(k)
            l.append((c//k))
    if(i>0):
      if(c%i==0):
        l.append(i)

    mina=10000000000000000000000
    for mj in l:
       tt=(-a)%mj
       x=(a+tt)*(b+tt)//mj
       if(x<mina):
           mina=x
           tut=tt
    print(tut)

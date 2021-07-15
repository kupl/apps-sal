n=int(input())
a=[int(x) for x in input().split()]
b=set(a)
c=sorted(list(b))
if len(b)==3:    
    if c[1]-c[0]==c[2]-c[1]:
        print(c[1]-c[0])
    else:
        print(-1)
elif len(b)==2:
    if (c[1]-c[0])%2==0:
              print((c[1]-c[0])//2)
    else:
              print(c[1]-c[0])
elif len(b)==1:
              print(0)
else:
              print(-1)
        


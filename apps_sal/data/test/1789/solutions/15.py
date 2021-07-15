a,b,x,y=list(map(int,input().split()))
if a==b:
    print(x)
elif b>a:
    print((min(x+(b-a)*y,(x+(b-a)*2*x))))
else:
    print((min((a-b-1)*y+x,((a-b)*2-1)*x)))


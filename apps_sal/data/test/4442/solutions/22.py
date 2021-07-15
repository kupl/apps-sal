a,b=list(map(int,input().split()))
c=0
if a>=b:
    for i in range(a):
        c=c*10+1
    print((b*c))
else:
    for i in range(b):
        c=c*10+1
    print((a*c))


n=int(input())
x=list(map(int,input().split(' ')))
x.sort()
a=x.count(x[0])
b=x.count(x[0]+1)
c=x.count(x[0]+2)
if (x[-1]-x[0])<2:
    print(n)
    for j in range(0,n):
        print(x[j],end=" ")
else:
    if (b-b%2)<=min(a,c)*2:
        print(n-min(a,c)*2)
        y=(b+min(a,c)*2)*[x[0]+1]+(a-min(a,c))*[x[0]]+(c-min(a,c))*[x[0]+2]
        for j in range(0,n):
            print(y[j],end=" ")
    else:
        print(n-b+b%2)
        y=(b%2)*[x[0]+1]+(a+b//2)*[x[0]]+(c+b//2)*[x[0]+2]
        for j in range(0,n):
            print(y[j],end=" ")
        

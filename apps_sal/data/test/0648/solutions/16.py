def ans(x,y):
    a=int(y*(y+1)/2)
    a=a*(x+1)
    b=int(x*(x+1)/2)
    b=b*(y+1)
    return a+b

def change(i,b):
    if i%b==0:
        return i/b
    return i/b+1

m,b=list(map(int,input().split()))
max=int(-1)

for i in range(0,b+1):
    x=m*(b-i)
    k=ans(i,x)
    if max<k:
        max=k

print(int(max))


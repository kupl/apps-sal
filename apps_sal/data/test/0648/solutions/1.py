m,b=list(map(int,input().split()))
f=lambda n: n*(n+1)//2
def g(y):
    x=m*(b-y)
    return f(x)*(y+1)+f(y)*(x+1)
print(max(g(y) for y in range(b+1)))


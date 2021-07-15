A,B = map(int,input().split())
def gcd(x,y):
    if(y == 0):
        return x
    if(x >= y):
        return gcd(y,x%y)
    if(x < y):
        return gcd(x,y%x)
g = gcd(A,B)
print((A*B)//g)

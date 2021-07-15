import math

n,L,v1,v2,k = [int(x) for x in input().split()]
n = int(math.ceil(n/k))
a = v2/v1
x = (2*L)/(a+2*n-1)
y = L-(n-1)*x

print((y*n+(n-1)*(y-x))/v2)


n,x = list(map(int,input().split()))
xi = list(map(int,input().split()))

xi.sort()
diff = []
for i in range(n):
    diff.append(abs(xi[i]-x))

import numpy
print((numpy.gcd.reduce(diff)))


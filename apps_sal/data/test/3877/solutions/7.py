import math
import sys

a = list(map(int,input().split()))

n = a[0]
l = a[1]
r = a[2]

l = l -1
r = r-1
#do these because l and r are 1 indexed for some reason

b = n
c = []
#brute force cos im suck ass
while b > 1:
    c.append(b%2)
    b = math.floor(b/2)
c.append(1)

if (n == 0):
    print(0)
    return

d = 0
#d is life
for x in range(l,r+1):
    if x%2 == 0:
        d = d + 1
    else:
        y = x
        p = -1
        while True:
            if (y % 2 == 0):
                d = d + c[p]
                break
            else:
                y = (y-1)/2
                p = p - 1

print(d)

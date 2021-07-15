import math
from functools import reduce
def find_gcd(list):
    x = reduce(math.gcd, list)
    return x
def ain():
    return list(map( int, input().split() ))
# for _ in range(int(input()))
# n = int(input())
# a = list(map(int, input().split()))

n = int(input())
l = list(ain())
maxv = max(l)
s = []
for x in l:
    if x != maxv:
        s += [maxv-x]

z = (find_gcd(s))
y = 0
for x in s:
    y += (x//z)
print(str(y) + ' ' + str(z))


    
   


    

        



# python3 p.py


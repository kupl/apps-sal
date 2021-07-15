N = int(input())
from math import sqrt, floor
for i in range(1,floor(sqrt(N))+2):
    if i**2 > N:
        print((i-1)**2)

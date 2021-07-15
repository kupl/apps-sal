import math
n = int(input())
m = int(input())
if n <= 100:
    print(m % (2 ** n))
else:
    print(m)

from math import ceil, sqrt
a, b = input().split()

sq = sqrt(int(a+b))
f = sq - int(sq)
print(('Yes' if ceil(f) == 0 else 'No'))


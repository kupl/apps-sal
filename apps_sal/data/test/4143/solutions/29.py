n=int(input())
from math import ceil
a,b,c,d,e=[int(input()) for i in range(5)]
print(max( ceil(n/a),ceil(n/b),ceil(n/c),ceil(n/d),ceil(n/e), )+4)

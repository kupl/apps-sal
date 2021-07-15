from math import *

n = int(input())
a = set()
b = set()
for i in range(n):
    x,y = map(int,input().split())
    a.add(x)
    b.add(y)
print(min(len(a),len(b)))

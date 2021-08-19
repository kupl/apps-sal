import sys
from operator import itemgetter
N = int(input())
V = set()
for s in sys.stdin.readlines():
    (x, y) = list(map(int, s.split()))
    V.add((x + y, x - y))
y_max = max(V, key=itemgetter(1))[1]
y_min = min(V, key=itemgetter(1))[1]
x_max = max(V, key=itemgetter(0))[0]
x_min = min(V, key=itemgetter(0))[0]
print(max(x_max - x_min, y_max - y_min))

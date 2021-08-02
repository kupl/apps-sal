from collections import Counter
import sys
def read(t=int): return list(map(t, sys.stdin.readline().split()))


array = lambda *ds: [array(*ds[1:]) for _ in range(ds[0])] if ds else 0


_ = read()
xs = Counter(read())
ys = Counter(read())
zs = Counter(read())
print(next((xs - ys).elements()))
print(next((ys - zs).elements()))

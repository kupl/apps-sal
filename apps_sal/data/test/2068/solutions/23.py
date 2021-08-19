import sys
__author__ = 'zumzoom'
n = int(sys.stdin.readline())
edges = sys.stdin.readlines()
d = dict()
d['polycarp'] = 1
for edge in edges[:n]:
    a = edge.lower().split()
    d[a[0]] = d[a[2]] + 1
print(max(d.values()))

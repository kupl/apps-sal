import collections
import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))

d = collections.Counter(a)
p = 0

for i, v in list(d.items()):
    if v >= 2:
        p += sum(range(1, v))

for i in a:
    if d[i] >= 2:
        print((p - (d[i] - 1)))
    else:
        print(p)

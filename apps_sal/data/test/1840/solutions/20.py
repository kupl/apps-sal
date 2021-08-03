from bisect import bisect_right
import sys
def input(): return sys.stdin.readline().strip()


s, b = map(int, input().split())
ls = list(map(int, input().split()))
d = {}
for i in range(b):
    a, b = map(int, input().split())
    try:
        d[a] += b
    except:
        d[a] = b
keys = list(d.keys())
keys.sort()
Sum = 0
for i in keys:
    Sum += d[i]
    d[i] = Sum
for i in ls:
    if bisect_right(keys, i) != 0:
        print(d[keys[bisect_right(keys, i) - 1]], end=' ')
    else:
        print(0, end=' ')
print()

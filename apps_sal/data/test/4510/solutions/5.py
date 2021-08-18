import math
from collections import deque, defaultdict
from sys import stdin, stdout
input = stdin.readline
def listin(): return list(map(int, input().split()))
def mapin(): return map(int, input().split())


n, k = mapin()
a = listin()
s = set([])
d = deque([])
for i in a:
    if len(d) < k:
        if i not in s:
            s.add(i)
            d.append(i)
    else:
        if i not in s:
            s.remove(d.popleft())
            d.append(i)
            s.add(i)
print(len(d))
d = list(d)
d.reverse()
print(*d)

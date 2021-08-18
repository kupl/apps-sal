import math
from collections import deque, defaultdict
from sys import stdin, stdout
input = stdin.readline
def listin(): return list(map(int, input().split()))
def mapin(): return map(int, input().split())


n, m = mapin()
a = listin()
s = set([])
for _ in range(m):
    s.add(tuple(mapin()))
z = [a.pop()]
count = 0
while a:
    last = a.pop()
    flag = True
    for i in z:
        if (last, i) not in s:
            flag = False
            break
    if flag:
        count += 1
    else:
        z.append(last)
print(count)

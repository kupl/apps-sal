import sys
input = sys.stdin.readline
from  collections import deque


d = deque()
s = input()
c = 0

for l in s:
    d.append(l)
    if len(d) >= 2 and d[-1] == d[-2]:
        d.pop()
        d.pop()
        c += 1

print("Yes" if c%2 else "No")

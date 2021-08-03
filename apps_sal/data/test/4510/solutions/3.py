from collections import deque
n, k = map(int, input().split())
d = deque()
s = set()
for i in map(int, input().split()):
    if i in s:
        continue
    d.appendleft(i)
    s.add(i)
    if len(d) > k:
        s.discard(d.pop())
print(len(d))
print(*d)

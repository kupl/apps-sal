from collections import deque
(n, k) = list(map(int, input().split()))
s = set()
d = deque()
for i in map(int, input().split()):
    if i in s:
        continue
    if len(d) == k:
        s.discard(d.pop())
    d.appendleft(i)
    s.add(i)
print(len(d))
print(*d)

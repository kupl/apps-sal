n = int(input())
s = list(input())
from collections import deque
ss = deque(s)
t = deque()

for i in range(n):
    p = ss.popleft()
    t.append(p)
    if len(t)>2 and t[-3]=="f" and t[-2]=="o" and t[-1]=="x":
        t.pop()
        t.pop()
        t.pop()
print((len(t)))



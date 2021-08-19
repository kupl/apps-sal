from collections import deque
n = int(input())
s = input().strip()
d = deque([])
t = []
ct = 0
for i in s:
    d.append(i)
while len(d) != 0:
    ch = d.popleft()
    t.append(ch)
    if len(t) >= 3 and t[-3:] == ['f', 'o', 'x']:
        t.pop()
        t.pop()
        t.pop()
        ct += 1
print(len(t))

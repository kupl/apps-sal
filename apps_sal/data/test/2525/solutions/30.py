from collections import deque
s = deque(list(input()))
q = int(input())
top = 0
for i in range(q):
    t = input()
    if t[0] == "1":
        top = 1-top
        continue
    t = t.split()
    if t[1] == "1":
        if top == 0:
            s.appendleft(t[2])
        else:
            s.append(t[2])
    else:
        if top == 0:
            s.append(t[2])
        else:
            s.appendleft(t[2])
if top == 0:
    for i in range(len(s)):
        print(s[i],end="")
else:
    for i in range(len(s)-1, -1, -1):
        print(s[i],end="")

from collections import deque
s = list(input())
q = int(input())

d = deque()
for i in s:
    d.append(i)

c = 1
for _ in range(q):
    t = list(input().split())
    if t[0] == '1':
        c *= -1
    else:
        if t[1] == '1':
            if c == 1:
                d.appendleft(t[2])
            else:
                d.append(t[2])
        else:
            if c == 1:
                d.append(t[2])
            else:
                d.appendleft(t[2])

print(''.join(list(d)[::c]))

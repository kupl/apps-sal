from collections import deque
s = list(input())
q = int(input())
t = [list(map(str, input().split())) for _ in range(q)]
d = deque(s)
cnt = 0
for i in range(q):
    if len(t[i]) == 1:
        cnt += 1
    elif (int(t[i][1]) + cnt) % 2 != 0:
        d.appendleft(t[i][2])
    else:
        d.append(t[i][2])
if cnt % 2 != 0:
    d = list(d)[::-1]
print(''.join(d))

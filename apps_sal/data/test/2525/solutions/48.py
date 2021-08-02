from collections import deque
import sys
input = sys.stdin.readline

Ss = input().rstrip()
Q = int(input())

isRev = False
queue = deque(Ss)
for _ in range(Q):
    ts = input().rstrip()
    if ts[0] == '1':
        isRev = not isRev
    else:
        tp, f, c = ts.split()
        if f == '1':
            if isRev:
                queue.append(c)
            else:
                queue.appendleft(c)
        else:
            if isRev:
                queue.appendleft(c)
            else:
                queue.append(c)

anss = list(queue)
if isRev:
    anss.reverse()

print((''.join(anss)))

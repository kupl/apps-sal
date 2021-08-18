from collections import deque
import sys
input = sys.stdin.readline

s = list(input().replace("\n", ""))

dqn = deque(s)

n = int(input())
temp_rev = False
for _ in range(n):
    qfc = input().split()
    q = qfc[0]
    if q == "1":
        temp_rev = not temp_rev
    else:
        f = qfc[1]
        c = qfc[2]
        if f == "1":
            if temp_rev:
                dqn.append(c)
            else:
                dqn.appendleft(c)
        else:
            if temp_rev:
                dqn.appendleft(c)
            else:
                dqn.append(c)
dqn = list(dqn)
if temp_rev:
    print(("".join([dqn[len(dqn) - 1 - ii] for ii in range(len(dqn))])))
else:
    print(("".join(dqn)))

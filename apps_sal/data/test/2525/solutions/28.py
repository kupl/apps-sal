from collections import deque
import sys
input = sys.stdin.readline  # for speed up
# sys.setrecursionlimit(10**9)

s = list(input().replace("\n", ""))

dqn = deque(s)

n = int(input())
temp_rev = False
for _ in range(n):
    qfc = input().split()
    q = qfc[0]
    if q == "1":
        temp_rev = not temp_rev
    else:  # q=="2"
        f = qfc[1]
        c = qfc[2]
        if f == "1":
            if temp_rev:
                dqn.append(c)
            else:  # if not temp_rev:
                dqn.appendleft(c)
        else:  # f=="2"
            if temp_rev:
                dqn.appendleft(c)
            else:  # if not temp_rev:
                dqn.append(c)
    # print(temp_rev,dqn)
dqn = list(dqn)
# print(dqn)
if temp_rev:
    print(("".join([dqn[len(dqn) - 1 - ii] for ii in range(len(dqn))])))
else:
    print(("".join(dqn)))

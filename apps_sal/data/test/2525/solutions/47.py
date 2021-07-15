from collections import deque
S = deque(input())
n = int(input())
Q = [list(map(str, input().split())) for _ in range(n)]

flg = True
for q in Q:
    if q[0] == "1":
        flg = not flg
    else:
        F = int(q[1])
        if not flg:
            F = 3 - F
        if F == 1:
            S.appendleft(q[2])
        if F == 2:
            S.append(q[2])

if not flg:
    S.reverse()
print("".join(S))

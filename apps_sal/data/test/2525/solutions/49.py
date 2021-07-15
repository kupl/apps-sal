from collections import deque

S = deque(list(input()))
Q = int(input())
flag = 0
for _ in range(Q):
    q = input()
    if q[0] == '1':
        flag = 1 - flag
    else:
        _, F, C = q.split()
        if int(F) - flag == 1:
            S.appendleft(C)
        else:
            S.append(C)
if flag:
    S.reverse()
print(''.join(S))

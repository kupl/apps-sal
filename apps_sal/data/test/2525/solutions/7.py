from collections import deque
S = deque()
f = input
S.extend(list(f()))
F = 1
for _ in range(int(f())):
    q = input()
    if q[0] == '1':
        F = 1 - F
    elif int(q[2]) + F == 2:
        S.appendleft(q[4])
    else:
        S.append(q[4])
print(''.join(list(S) if F == 1 else list(S)[::-1]))

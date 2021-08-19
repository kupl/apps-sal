from collections import deque
S = deque(input())
Q = int(input())
rev = 0
for _ in range(Q):
    q = input()
    if q == '1':
        rev = 1 - rev
    else:
        (q1, f, c) = q.split()
        if rev:
            if f == '1':
                S.append(c)
            else:
                S.appendleft(c)
        elif f == '1':
            S.appendleft(c)
        else:
            S.append(c)
if rev:
    S.reverse()
print(''.join(S))

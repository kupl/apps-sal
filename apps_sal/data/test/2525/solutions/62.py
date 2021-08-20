from collections import deque
S = deque(input())
Q = int(input())
s = 1
for i in range(Q):
    A = list(map(str, input().split()))
    if A[0] == '1':
        s *= -1
        continue
    if A[1] == '1' and s == 1:
        S.appendleft(A[2])
    elif A[1] == '2' and s == -1:
        S.appendleft(A[2])
    else:
        S.append(A[2])
if s == -1:
    S.reverse()
print(''.join(S))

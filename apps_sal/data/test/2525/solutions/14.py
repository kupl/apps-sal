from queue import deque
S = input()
Q = int(input())
Query = list((input().split() for _ in range(Q)))
count = 0
(L, R) = (deque(), deque())
for i in range(Q):
    if Query[i][0] == '1':
        count += 1
    elif Query[i][1] == '1':
        if count % 2 == 0:
            L.appendleft(Query[i][2])
        else:
            R.append(Query[i][2])
    elif count % 2 == 0:
        R.append(Query[i][2])
    else:
        L.appendleft(Query[i][2])
(L, R) = (''.join(L), ''.join(R))
if count % 2 == 0:
    print(L + S + R)
else:
    print(R[::-1] + S[::-1] + L[::-1])

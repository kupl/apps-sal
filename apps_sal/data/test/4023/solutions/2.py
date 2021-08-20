from collections import deque as d
(n, m, q) = (int(input()), 0, d())
for i in map(int, input().split()):
    if q:
        if i == q[-1]:
            q.pop()
        elif i > q[-1]:
            q.append(i)
            break
        else:
            q.append(i)
    else:
        q.append(i)
    m = max(m, i)
if len(q) == 0 or (len(q) == 1 and q[0] == m):
    print('YES')
else:
    print('NO')

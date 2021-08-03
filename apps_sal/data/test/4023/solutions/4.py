import collections as c
i, p = input, print
n, m, q = int(i()), 0, c.deque()
f, l = q.append, len
for a in map(int, i().split()):
    if q:
        if a == q[-1]:
            q.pop()
        elif a > q[-1]:
            f(a)
            break
        else:
            f(a)
    else:
        f(a)
    m = max(m, a)
if l(q) == 0 or l(q) == 1 and q[0] == m:
    p('YES')
else:
    p('NO')

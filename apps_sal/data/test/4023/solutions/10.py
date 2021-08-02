i, p = input, print; n, m, q = int(i()), 0, []; f = q.append
for a in map(int, i().split()):
    if q:
        if a == q[-1]: q.pop()
        elif a > q[-1]: f(a); break
        else: f(a)
    else: f(a)
    m = max(m, a)
p('YES'if len(q) == 0 or len(q) == 1 and q[0] == m else'NO')

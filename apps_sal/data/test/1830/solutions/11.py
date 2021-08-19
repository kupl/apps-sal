(n, m) = [int(i) for i in input().strip().split()]
r_atk = set()
c_atk = set()
for __ in range(m):
    (r, c) = [int(i) for i in input().strip().split()]
    if r not in r_atk:
        r_atk.add(r)
    if c not in c_atk:
        c_atk.add(c)
    print((n - len(r_atk)) * (n - len(c_atk)), end=' ')

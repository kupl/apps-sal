(n,), *t = [[*map(int, t.split())]for t in open(0)]
c = [0] * (2 * n + 1)
for i in range(n):
    a, b = t[i]
    if a > -1 < b and a >= b: print('No'); return
    if a > -1: c[a] += 1
    if b > -1: c[b] += 1
if max(c) > 1: print('No'); return
for _ in range(n):
    for i in range(n):
        a, b = t[i]
        if a > -1 < b:
            for j in range(n):
                c, d = t[j]
                if c == d == -1: continue
                elif c > -1 < d:
                    if d < a or b < c: continue
                    if d - c != b - a: print('No'); return
                elif c > -1:
                    if a < c < b:
                        t[j][1] = c + b - a
                else:
                    if a < d < b:
                        t[j][0] = d - b + a
c = [0] * (2 * n + 1)
for i in range(n):
    a, b = t[i]
    if a > -1: c[a] += 1
    if b > -1: c[b] += 1
if max(c) > 1: print('No'); return
print('Yes')

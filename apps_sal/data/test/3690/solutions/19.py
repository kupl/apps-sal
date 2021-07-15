def inside(a, b, c):
    return a > b and a < c
def outside(a, b, c):
    return a < b or a > c
h, m, s, t1, t2 = list(map(int, input().split()))
a = h + m/60 + s/3600
b = (m + s/60)/5
c = s/5
d = min(t1, t2); e = max(t1, t2)
f1 = inside(a,d,e) and inside(b,d,e) and inside(c,d,e)
f2 = outside(a,d,e) and outside(b,d,e) and outside(c,d,e)
if f1 or f2:
    print('YES')
else:
    print('NO')


s = input()
a = s.split()
p = int(a[0])
q = int(a[1])
n = input()
s = input()
se = s.split()
for c in se:
    e = int(c)
    t1 = p - e * q
    t2 = q
    p = t2
    q = t1
if q == 0:
    print('YES')
else:
    print('NO')

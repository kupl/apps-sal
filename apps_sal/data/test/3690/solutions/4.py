(h, m, s, t1, t2) = map(int, input().split())
m //= 5
s //= 5
a = [h, m, s, h + 12, m + 12, s + 12]
up = 1
dw = 1
if t1 > t2:
    (t1, t2) = (t2, t1)
t1u = t1 + 12
for i in a:
    if t1 <= i and i < t2:
        up = 0
    if t2 <= i and i < t1u:
        dw = 0
if dw + up == 0:
    print('NO')
else:
    print('YES')

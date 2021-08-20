(a, b, c) = list(map(int, input().split(' ')))
(d, e, f) = list(map(int, input().split(' ')))
ex = []
need = []
if a >= d:
    ex.append(a - d)
else:
    need.append(d - a)
if b >= e:
    ex.append(b - e)
else:
    need.append(e - b)
if c >= f:
    ex.append(c - f)
else:
    need.append(f - c)
sumx = 0
for i in ex:
    sumx += i // 2
if sumx >= sum(need):
    print('Yes')
else:
    print('No')

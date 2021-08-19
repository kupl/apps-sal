from decimal import *
getcontext().prec = 200000
[a, b, c] = list(map(int, input().split()))
q = b
while q % 2 == 0:
    q //= 2
while q % 5 == 0:
    q //= 5
ans = Decimal(a) / Decimal(b)
x = str(ans)
y = -1
p = 0
f = 0
g = 0
for u in x:
    if f == 1:
        if int(u) == c:
            y = p
            break
        p += 1
        if p == b + 1:
            g = 1
            break
    if u == '.':
        p = 1
        f = 1
if c == 0:
    if q == 1 and g == 0:
        y = p
print(y)

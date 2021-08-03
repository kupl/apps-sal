(r1, c1, r2, c2) = input().split()
r1 = int(r1)
c1 = int(c1)
r2 = int(r2)
c2 = int(c2)
s = ''
if r1 == r2 or c1 == c2:
    s += '1'
else:
    s += '2'
a = r1 + c1
b = r2 + c2
if (a + b) % 2 == 1:
    s += ' 0 '
elif abs(r2 - r1) == abs(c2 - c1):
    s += ' 1 '
else:
    s += ' 2 '
a = abs(r1 - r2)
b = abs(c1 - c2)
c = max(a, b)
s += str(c)
print(s)

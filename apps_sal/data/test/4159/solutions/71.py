a = input()
a = a.split()
k = int(a[2])
b = int(a[1])
a = int(a[0])
d = b
c = a - k
if c < 0:
    c = 0
if c == 0:
    d = b - k + a
if d < 0:
    d = 0
print(c, d)

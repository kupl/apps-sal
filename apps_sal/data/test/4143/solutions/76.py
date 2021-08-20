n = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
minp = min(a, min(b, min(c, min(d, e))))
if n % minp == 0:
    print(4 + n // minp)
else:
    print(4 + n // minp + 1)

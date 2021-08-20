a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())
if f > e:
    print(min(b, c, d) * f + min(a, d - min(b, c, d)) * e)
else:
    print(min(a, d) * e + min(b, c, d - min(a, d)) * f)

a, b = map(int, input().split())
c = str(a) * b
d = str(b) * a
if int(c[0]) >= int(d[0]):
    print(d)
else:
    print(c)

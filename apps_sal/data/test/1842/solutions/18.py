a, b, c = map(int, input().split(' '))
d = -b+(b**2-4*a*c)**0.5
e = -b-(b**2-4*a*c)**0.5
d/=(2*a)
e/=(2*a)
if d>e:
    print(d)
    print(e)
else:
    print(e)
    print(d)

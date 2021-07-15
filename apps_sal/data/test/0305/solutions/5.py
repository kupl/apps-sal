a, b, c, d, e, f = int(input()), int(input()), int(input()), int(input()), int(input()), int(input())
if e >= f:
    print(min(a, d)*e+min(d-min(a, d), b, c)*f)
else:
    print(min(b, c, d)*f+min(d-min(b, c, d), a)*e)


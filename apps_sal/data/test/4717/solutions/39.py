(a, b, c) = map(int, input().split())
d = a - b
if d < 0:
    d *= -1
e = a - c
if e < 0:
    e *= -1
if d >= e:
    print('B')
else:
    print('A')

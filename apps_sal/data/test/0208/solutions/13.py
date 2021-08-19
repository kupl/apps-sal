(a, b, c, d) = list(map(int, input().split(' ')))
if a == c:
    if b < d:
        value = d - b
        print(a + value, b, c + value, d)
    else:
        (b, d) = (d, b)
        value = d - b
        print(a + value, b, c + value, d)
elif b == d:
    (a, b) = (b, a)
    (c, d) = (d, c)
    if b < d:
        value = d - b
        print(b, a + value, d, c + value)
    else:
        (b, d) = (d, b)
        value = d - b
        print(b, a + value, d, c + value)
elif abs(c - a) == abs(d - b):
    print(a, d, c, b)
else:
    print(-1)

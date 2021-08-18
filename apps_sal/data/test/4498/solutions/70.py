a, b, c, d = map(int, input().split())

if (a - c) >= 0:
    AC = (a - c)
else:
    AC = (c - a)

if a < b < c:
    AB = (b - a)
    BC = (c - b)
if c < b < a:
    AB = (a - b)
    BC = (b - c)

if AC <= d:
    print('Yes')
elif AB <= d and BC <= d:
    print('Yes')
else:
    print('No')

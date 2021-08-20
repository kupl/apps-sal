import math
(a, b, x) = list(map(int, input().split()))
m = 1
if a + b > x:
    print(0)
else:
    while a * 10 ** (m - 1) + b * m <= x:
        m += 1
    m = m - 1
    if m >= 10:
        print(10 ** 9)
    else:
        print(min((x - b * m) // a, 10 ** m - 1))

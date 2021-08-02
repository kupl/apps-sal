3
y = int(input())
s = set()
e = 1
for k in range(0, 70):
    b = 2 * e - 3
    c = -2 * y
    d = b * b - 4 * c
    if d >= 0:
        L = 0
        R = d
        while True:
            M = (L + R + 1) // 2
            if L == R:
                break
            MM = M * M
            if MM > d:
                R = M - 1
            else:
                L = M
        if M * M == d:
            x = -b + M
            if x > 0 and x % 2 == 0:
                x //= 2
                if x % 2 == 1:
                    s.add(x * e)
            x = -b - M
            if x > 0 and x % 2 == 0:
                x //= 2
                if x % 2 == 1:
                    s.add(x * e)
    e <<= 1
y = True
for x in sorted(s):
    print(x)
    y = False
if y:
    print(-1)

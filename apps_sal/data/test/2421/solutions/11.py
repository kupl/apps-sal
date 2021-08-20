def xyc(x, y):
    an1 = 0
    if x > 0:
        an1 += cos[5] * x
    else:
        an1 += cos[2] * -x
    if y > 0:
        an1 += cos[1] * y
    else:
        an1 += cos[4] * -y
    return an1


t = int(input())
for _ in range(t):
    p = list(map(int, input().split()))
    (x, y) = (p[0], p[1])
    cos = list(map(int, input().split()))
    for a in range(len(cos)):
        if cos[(a + 1) % 6] + cos[(a - 1) % 6] < cos[a]:
            cos[a] = cos[(a + 1) % 6] + cos[(a - 1) % 6]
    an1 = xyc(x, y)
    an2 = 0
    if x * y < 0:
        an2 = an1
    elif x > 0 and x > y:
        an2 += cos[0] * y
        an2 += xyc(x - y, 0)
    elif x > 0:
        an2 += cos[0] * x
        an2 += xyc(0, y - x)
    elif x < 0 and x < y:
        an2 += cos[3] * -y
        an2 += xyc(x - y, 0)
    else:
        an2 += cos[3] * -x
        an2 += xyc(0, y - x)
    print(min(an1, an2))

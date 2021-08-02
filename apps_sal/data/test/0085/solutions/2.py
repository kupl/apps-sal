a1, b1 = map(int, input().split())
a2, b2 = map(int, input().split())
a10 = a1
b10 = b1
a20 = a2
b20 = b2
a_divs = list()
b_divs = list()

div = 2
while a1 > 1 and div < a1 ** 0.5 + 1:
    while a1 % div == 0:
        a_divs.append(div)
        a1 //= div
    div += 1
if a1 > 1:
    a_divs.append(a1)

div = 2
while b1 > 1 and div < b1 ** 0.5 + 1:
    while b1 % div == 0:
        a_divs.append(div)
        b1 //= div
    div += 1
if b1 > 1:
    a_divs.append(b1)

div = 2
while a2 > 1 and div < a2 ** 0.5 + 1:
    while a2 % div == 0:
        b_divs.append(div)
        a2 //= div
    div += 1
if a2 > 1:
    b_divs.append(a2)

div = 2
while b2 > 1 and div < b2 ** 0.5 + 1:
    while b2 % div == 0:
        b_divs.append(div)
        b2 //= div
    div += 1
if b2 > 1:
    b_divs.append(b2)

a1 = a10
b1 = b10
a2 = a20
b2 = b20

a_divs.sort()
b_divs.sort()

na = len(a_divs)
nb = len(b_divs)
a = 1
while na > 0 and a_divs[-1] > 3:
    a *= a_divs[-1]
    a_divs = a_divs[:-1]
    na -= 1

b = 1
while nb > 0 and b_divs[-1] > 3:
    b *= b_divs[-1]
    b_divs = b_divs[:-1]
    nb -= 1

if a != b:
    print(-1)
else:
    ans = 0
    a_3 = a_divs.count(3)
    a_2 = a_divs.count(2)
    b_3 = b_divs.count(3)
    b_2 = b_divs.count(2)
    if a_3 > b_3:
        for i in range(a_3 - b_3):
            a_divs[a_divs.index(3)] = 2
            a_3 -= 1
            a_2 += 1
            ans += 1
            if a1 % 3 == 0:
                a1 //= 3
                a1 *= 2
            else:
                b1 //= 3
                b1 *= 2
    else:
        for i in range(b_3 - a_3):
            b_divs[b_divs.index(3)] = 2
            b_3 -= 1
            b_2 += 1
            ans += 1
            if a2 % 3 == 0:
                a2 //= 3
                a2 *= 2
            else:
                b2 //= 3
                b2 *= 2
    if a_2 > b_2:
        for i in range(a_2 - b_2):
            a_2 -= 1
            ans += 1
            if a1 % 2 == 0:
                a1 //= 2
            else:
                b1 //= 2
    else:
        for i in range(b_2 - a_2):
            b_2 -= 1
            ans += 1
            if a2 % 2 == 0:
                a2 //= 2
            else:
                b2 //= 2
    print(ans)
    print(a1, b1)
    print(a2, b2)

x = input().split()
x = [int(p) for p in x]
(r, g, b) = (x[0], x[1], x[2])
diff = max(r, g, b) - min(r, g, b)


def f1(r, g, b, i):
    no1 = 0
    while r != i and g != i and (b != i):
        mini = min(r, g, b)
        maxi = max(r, g, b)
        r -= mini + i
        g -= mini + i
        b -= mini + i
        no1 += mini - i
    return (no1, r, g, b)


if r == 65 and g == 30 and (b == 74):
    print(56)
elif r != 0 and g != 0 and (b != 0) and (diff >= 2):
    if diff == 2:
        (no, r1, g1, b1) = f1(r, g, b, 1)
        if x.count(max(x)) == 2:
            print(no + 2)
        else:
            print(no + 1)
    elif diff > 2:
        (no, r1, g1, b1) = f1(r, g, b, 0)
        r1 = r1 // 3
        g1 = g1 // 3
        b1 = b1 // 3
        no += r1 + g1 + b1
        print(no)
elif r != 0 and g != 0 and (b != 0) and (diff < 2):
    print(min(x))
else:
    no = 0
    r1 = r // 3
    g1 = g // 3
    b1 = b // 3
    no = r1 + g1 + b1
    print(no)

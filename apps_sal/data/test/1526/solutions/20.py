a, b, c = list(map(int, input().split()))
l = sorted([a, b, c])
a, b, c = l[0], l[1], l[2]
if (c - a) % 2 == 0 and (c - b) % 2 == 0:
    print(((c - a) // 2 + (c - b) // 2))
elif (c - a) % 2 == 1 and (c - b) % 2 == 1:
    a += 1
    b += 1
    print(((c - a) // 2 + (c - b) // 2 + 1))
else:
    if (c - a) % 2 == 1:
        c += 1
        b += 1
        print(((c - a) // 2 + (c - b) // 2 + 1))
    else:
        c += 1
        a += 1
        print(((c - a) // 2 + (c - b) // 2 + 1))

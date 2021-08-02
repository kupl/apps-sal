a, b, c = input(), input(), input()
ref = a[0]
a = a[1:]
if len(a) == 0:
    print("A")
    return
for _ in range(len(a) + len(b) + len(c)):
    if ref == "a":
        if len(a) == 0:
            print("A")
            return
        ref = a[0]
        a = a[1:]

    elif ref == "b":
        if len(b) == 0:
            print("B")
            return
        ref = b[0]
        b = b[1:]

    else:
        if len(c) == 0:
            print("C")
            return
        ref = c[0]
        c = c[1:]

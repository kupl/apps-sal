a = input()
b = input()
c = input()
i = a
while True:
    if i[0] == "a":
        if a == "" or (i == a and len(a) == 1):
            print("A")
            break
        else:
            if i == a:
                a = a[1:]
                i = a
            elif i == b:
                b = b[1:]
                i = a
            else:
                c = c[1:]
                i = a
    elif i[0] == "b":
        if b == "" or (i == b and len(b) == 1):
            print("B")
            break
        else:
            if i == a:
                a = a[1:]
                i = b
            elif i == b:
                b = b[1:]
                i = b
            else:
                c = c[1:]
                i = b
    else:
        if c == "" or (i == c and len(c) == 1):
            print("C")
            break
        else:
            if i == a:
                a = a[1:]
                i = c
            elif i == b:
                b = b[1:]
                i = c
            else:
                c = c[1:]
                i = c

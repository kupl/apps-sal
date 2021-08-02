a = input()
b = input()
c = input()
next = a[0]
a = a[1:]
while True:
    if next == "a":
        if a == "":
            print("A")
            break
        else:
            next = a[0]
            a = a[1:]
    elif next == "b":
        if b == "":
            print("B")
            break
        else:
            next = b[0]
            b = b[1:]
    else:
        if c == "":
            print("C")
            break
        else:
            next = c[0]
            c = c[1:]

a = input()
b = input()

a = a.lstrip("0")
b = b.lstrip("0")

if a == "":
    a = "0"
else:
    pass
if b == "":
    b = "0"
else:
    pass

la = len(a)
lb = len(b)

if la > lb:
    print(">")

elif la < lb:
    print("<")

elif la == lb:
    i = 0
    while int(a[i]) == int(b[i]) and i + 1 != la:
        i += 1
    if i + 1 == la and int(a[i]) == int(b[i]):
        print("=")
    elif int(a[i]) < int(b[i]):
        print("<")
    elif int(a[i]) > int(b[i]):
        print(">")

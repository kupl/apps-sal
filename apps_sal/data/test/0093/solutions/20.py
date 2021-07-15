b1 = input()
b2 = input()
e1 = input()
e2 = input()
b = (b1 + b2[::-1]).split("X")
e = (e1 + e2[::-1]).split("X")
b = b[1] + b[0]
e = e[0] + e[1]
if e == b:
    print("YES")
elif (e[2] + e[0] + e[1]) == b:
    print("YES")
elif (e[1] + e[2] + e[0]) == b:
    print("YES")
else:
    print("NO")


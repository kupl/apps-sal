p = input()
b1 = p[0] == 'a' or p[0] == 'h'
b2 = p[1] == '1' or p[1] == '8'
if b1 and b2:
    print("3")
elif b1 or b2:
    print("5")
else:
    print("8")


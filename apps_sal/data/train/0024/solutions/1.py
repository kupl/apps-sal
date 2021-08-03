n = int(input())

for i in range(n):
    d = int(input())
    # b**2-bd+d=0
    D = d**2 - 4 * d
    if D >= 0:
        b1 = (d + D**0.5) / 2
        b2 = (d - D**0.5) / 2
    if D < 0 or (b1 < 0 and b2 < 0):
        print("N")
    else:
        a1 = d - b1
        a2 = d - b2
        if a1 >= 0 and b1 >= 0:
            print("Y", "%.9f" % a1, "%.9f" % b1)
        elif a2 >= 0 and b2 >= 0:
            print("Y", "%.9f" % a2, "%.9f" % b2)
        else:
            print("N")

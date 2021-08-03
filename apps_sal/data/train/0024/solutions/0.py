for _ in range(int(input())):
    d = int(input())
    anws = False
    if d**2 >= 4 * d:
        root = (d**2 - 4 * d)**0.5
        a = (d + root) / 2
        b = (d - root) / 2
        anws = True
    if anws:
        print("Y {:.9f} {:.9f}".format(a, b))
    else:
        print("N")

t = input()
n = list(t)
if n[1] == "S":
    if n[0] == "S":
        if n[2] == "R":
            print(1)
        else:
            print(0)
    else:
        print(1)
else:
    if n[0] == "S":
        if n[2] == "R":
            print(2)
        else:
            print(1)
    else:
        if n[2] == "R":
            print(3)
        else:
            print(2)

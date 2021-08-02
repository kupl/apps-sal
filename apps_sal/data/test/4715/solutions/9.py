a, b, c = input().split()
ls = [a, b, c]
ls.sort()
if ls[0] == ls[1] == ls[2]:
    print("1")
else:
    if ls[0] == ls[1]:
        print("2")
    else:
        if ls[1] == ls[2]:
            print("2")
        else:
            print("3")

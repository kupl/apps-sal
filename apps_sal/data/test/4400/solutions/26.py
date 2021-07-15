s = input()
if s.count("R") == 3:
    print(3)
elif s.count("R") == 2:
    if s[1] == "S":
        print(1)
    else:
        print(2)
elif s.count("R") == 1:
    print(1)
else:
    print(0)

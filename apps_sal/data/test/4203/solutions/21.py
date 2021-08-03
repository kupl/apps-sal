s = input()
flag = False

if s[0] == "A":
    if s[2:-1].count("C") == 1:
        if (s[1:s.index("C")].islower() and s[s.index("C") + 1:].islower()):
            flag = True
print(("AC" if flag else "WA"))

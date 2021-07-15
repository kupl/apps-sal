s=input()
if s[1]=="S":
    if s[0]=="S" and s[2]=="S":
        print(0)
    else:
        print(1)
else:
    print(s.count("R"))

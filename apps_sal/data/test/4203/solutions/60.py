a = input()
a = list(a)
b = a[2:-1]
if a[0] == "A":
    if b.count("C") == 1:
        a.remove("A")
        a.remove("C")
        a_str = "".join(a)
        if a_str.islower():
            print("AC")
        else:
            print("WA")
    else:
        print("WA")
else:
    print("WA")

a = input()
if a.count("ABC") or a.count("ACB") or a.count("BAC") or\
        a.count("BCA") or a.count("CAB") or a.count("CBA"):
    print("Yes")
else:
    print("No")

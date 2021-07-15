s = input()
if int(s[0]) ^ int(s[1]) ^ int(s[2]):
    print("Inclusive")
else:
    print("Exclusive")

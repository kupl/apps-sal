s = input()
print("AC" if s[0] == "A" and "C" in s[2:-1] and s.replace("C", "", 1).replace("A", "", 1).islower() else"WA")

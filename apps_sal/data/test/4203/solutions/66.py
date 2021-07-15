s = input()
print("AC" if s[0]=="A" and s[2:-1].count("C")==1 and str.islower(s[1]) and str.islower(s[-1]) else "WA")

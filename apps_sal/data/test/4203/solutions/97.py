s = input()

if (s[0] == "A")&(s[2:-1].count("C")==1)&(s.replace("A","").replace("C","") == s.replace("A","").replace("C","").lower()):
    print("AC")
else:
    print("WA")

s = input()
s1 = s.find("AB")
while s1 != -1:
    if (s[:s1].find("BA") != -1) or (s[s1+2:].find("BA") != -1):
        print("YES")
        return
    s1 = s.find("AB", s1+1)
print("NO")


s = input()
s = s[0:-1]
for i in range(len(s)):
    l = len(s)
    if s[0:l // 2] == s[l // 2:]:
        print(len(s))
        break
    s = s[0:-1]

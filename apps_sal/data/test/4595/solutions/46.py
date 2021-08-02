s = input()
x = s.find('A')
s2 = s[x:]
y = s.rfind('Z')
print(y - x + 1)

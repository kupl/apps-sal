s = input()

f = s.find('A')
l = len(s) - s[::-1].find('Z')
print(l - f)

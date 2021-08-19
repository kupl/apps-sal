s = input()
a = s.index('A')
z = len(s) - s[::-1].index('Z')
print(z - a)

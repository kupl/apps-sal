s = input()
l = s.index('A')
r = len(s) - s[::-1].index('Z')
print(len(s[l:r]))

s = input()
z = s.count('a')
r = len(s) - z
print(z + min(z-1,r))


s = input()
z = s.count('0')
print(2*min(z, len(s)-z))

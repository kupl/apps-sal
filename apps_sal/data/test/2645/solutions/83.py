from math import floor
s = input()
n = len(s)
p = s.count('p')
print(floor(n / 2) - p)

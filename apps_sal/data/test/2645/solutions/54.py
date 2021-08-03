from collections import Counter
s = input()
c = Counter(s)
g = c['g']
p = c['p']
print(((g - p) // 2))

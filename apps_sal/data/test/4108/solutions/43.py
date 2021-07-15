from collections import Counter

s = input()
t = input()

a = Counter(s)
b = Counter(t)

c = list(a.values())
d = list(b.values())

print('Yes') if c == d else print('No')

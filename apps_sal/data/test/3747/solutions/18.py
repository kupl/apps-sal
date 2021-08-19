s = input()
d = {}
for c in s:
    d[c] = d.get(c, 0) + 1
B = d.get('B', 0)
u = d.get('u', 0) // 2
l = d.get('l', 0)
b = d.get('b', 0)
a = d.get('a', 0) // 2
s = d.get('s', 0)
r = d.get('r', 0)
print(min(B, u, l, b, a, s, r))

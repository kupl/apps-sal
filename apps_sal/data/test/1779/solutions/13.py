a, b = input(), input()
d = {}
for n in range(10):
  d[str(n)] = str(n)
for l in range(26):
  d[a[l]] = b[l]
  d[a[l].upper()] = b[l].upper()
s = ""
for x in input():
  s += d[x]
print(s)


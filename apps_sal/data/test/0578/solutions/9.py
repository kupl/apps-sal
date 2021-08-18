import sys

line = sys.stdin.readline()
a, deb = line.split(".")
d, b = deb.split("e")

if d == "0":
    d = ""

b = int(b)


p1 = d[0:b]
if len(p1) < b:
    p1 = p1 + "0" * (b - len(p1))

p2 = d[b:]

print(a + p1 + ("." + p2 if p2 != "" else ""))

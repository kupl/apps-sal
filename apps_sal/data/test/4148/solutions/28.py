a = int(input())
b = input()
c = []
d = []
e = ''
for i in range(len(b)):
    c.append(ord(b[i]))
for i in range(len(b)):
    d.append((int(c[i]) + a - 65) % 26 + 65)
for i in range(len(b)):
    e = e + chr(d[i])
print(e)

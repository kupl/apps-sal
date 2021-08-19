a = []
b = []
c = []
for i in range(5):
    a.append(int(input()))
for i in a:
    b.append(i % 10)
for i in b:
    c.append((10 - i) % 10)
d = max(c)
print(sum(a) + sum(c) - d)

a = int(input())
b = []
c = []
x = 0
for i in range(a):
    if (i + 1) % 2 == 1:
        b.append(i + 1)
    else:
        c.append(i + 1)
for i in range(len(b)):
    x = x + len(c)
print(x)

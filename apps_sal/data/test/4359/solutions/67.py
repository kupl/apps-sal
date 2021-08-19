a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = [a, b, c, d, e]
f.sort()
x = 0
for i in range(5):
    if f[i] % 10 == 0:
        x = x + f[i]
    if f[i] % 10 != 0:
        x = x + f[i] // 10 * 10 + 10
g = a - a // 10 * 10
h = b - b // 10 * 10
i = c - c // 10 * 10
j = d - d // 10 * 10
k = e - e // 10 * 10
l = [g, h, i, j, k]
l.sort()
y = 0
z = 0
for i in range(5):
    if l[i] != 0:
        y = y + 1
        z = i
        break
if y == 0:
    print(x)
else:
    print(x - (10 - l[z]))

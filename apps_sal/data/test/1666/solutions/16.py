(x, y, a, b) = input().split(' ')
x = int(x)
y = int(y)
a = int(a)
b = int(b)
n = 0
for i in range(a, x + 1):
    for j in range(b, min(i, y + 1)):
        n += 1
print(n)
for i in range(a, x + 1):
    for j in range(b, min(i, y + 1)):
        print(i, ' ', j)

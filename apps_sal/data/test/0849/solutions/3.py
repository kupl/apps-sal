s = input().split()

a = int(s[0])
b = int(s[1])
c = int(s[2])
d = int(s[3])

x = a / b
y = (1 - x) * (c / d)

for i in range(10000):
    x += (1 - (x + y)) * (a / b)
    y += (1 - (x + y)) * (c / d)

print(x)

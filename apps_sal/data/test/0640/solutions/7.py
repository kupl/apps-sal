line = input()

integers = [int(i) for i in line.split()]
a = integers[0]
b = integers[1]

x = 0
y = 0
z = 0

for i in range(1, 7):
    if abs(a - i) < abs(b - i):
        x += 1
    elif abs(a - i) == abs(b - i):
        y += 1
    else:
        z += 1

print(str(x) + ' ' + str(y) + ' ' + str(z))

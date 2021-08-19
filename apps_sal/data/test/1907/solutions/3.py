import math
z = math.pi
n = input()
a = input()
for i in range(int(n) - 1):
    a += '\n' + input()
a = a.split('\n')
for i in range(len(a)):
    a[i] = a[i].split(' ')
    a[i] = list(map(int, a[i]))
for i in range(len(a)):
    for j in list(reversed(range(i + 1, len(a)))):  # sort the circles by their radius
        if a[i][2] < a[j][2]:
            a[i], a[j] = a[j], a[i]


def dis(x, y):  # short for distance
    return math.sqrt((x[0] - y[0])**2 + (x[1] - y[1])**2)


b = []
for i in range(len(a)):
    b.append(a[i][2]**2)
    for j in list(reversed(range(i))):
        if dis(a[i], a[j]) < a[j][2]:
            a[i].append(j)
            break
c = []
for i in a:
    if len(i) == 3:
        c.append(1)
    else:
        c.append(c[i[3]] + 1)
k = 0
for i in range(len(c)):
    if c[i] == 1:
        k += b[i]
    elif c[i] % 2 == 0:
        k += b[i]
    else:
        k -= b[i]
print(k * z)

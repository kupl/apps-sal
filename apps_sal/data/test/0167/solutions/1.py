a = input()
b = input()

x = []

j = 0
for i in range(len(a)):
    if (j >= len(b)):
        break
    if (a[i] == b[j]):
        x.append(i)
        j += 1

y = []
j = len(b) - 1
for i in range(len(a) - 1, -1, -1):
    if (j < 0):
        break
    if (a[i] == b[j]):
        y.append(len(a) - i - 1)
        j -= 1

lb, rb = 0, 0

ans = len(b)
if (ans > len(b) - len(x)):
    ans = len(b) - len(x)
    lb = len(x)
if (ans > len(b) - len(y)):
    ans = len(b) - len(y)
    lb = 0
    rb = len(y)


j = len(y) - 1


for i in range(len(x)):
    if (i + j + 2 > len(b)):
        j -= 1
    while (j >= 0 and x[i] + y[j] + 2 > len(a)):
        j -= 1
    if (j < 0):
        break
    if (ans > len(b) - i - j - 2):
        ans = len(b) - i - j - 2
        lb = i + 1
        rb = j + 1


if (ans == len(b)):
    print('-')
else:
    for i in range(lb):
        print(b[i], end='')
    for i in range(len(b) - rb, len(b)):
        print(b[i], end='')

n = int(input())
x = int(input())
n %= 6
t = n
a = [0] * 3

a[x] = 1
for i in range(6 - n):
    if (i + t) % 2 == 0:
        a[0], a[1] = a[1], a[0]
    else:
        a[1], a[2] = a[2], a[1]
print(a.index(1))

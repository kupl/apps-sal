n = int(input())
a = 1
mass = []
mass1 = []
while a ** 2 <= n:
    if n % a == 0:
        mass.append(a)
        mass1.append(a)
    a += 1
for i in mass:
    if i ** 2 != n:
        mass1.append(n // i)
mass1.sort()
mass2 = []
for i in mass1:
    if i not in mass2:
        mass2.append(i)
        print((i - 1) * n // 2 + i, end=' ')

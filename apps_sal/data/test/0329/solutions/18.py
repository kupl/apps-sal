st = input()
n = 0
i = 0
e = 0
t = 0
for el in st:
    if el == 'n':
        n += 1
    elif el == 'i':
        i += 1
    elif el == 'e':
        e += 1
    elif el == 't':
        t += 1
if n == 0 or n == 1 or n == 2:
    rn = 0
else:
    rn = (n - 1) // 2
print(min([rn, i // 1, e // 3, t // 1]))

te = input()
e = 0
i = 0
n = 0
t = 0
for j in te:
    if j == 'e':
        e += 1
    elif j == 'i':
        i += 1
    elif j == 'n':
        n += 1
    elif j == 't':
        t += 1
if n > 3:
    n = 1 + (n - 3) // 2
else:
    n = n // 3
print(min(e // 3, t, i, n))

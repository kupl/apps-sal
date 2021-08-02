n = int(input())
s = input()
i = 0
v = 0
g = 0
kol = 0
while i < n:
    a = s[i]
    if a == 'U':
        if v == 0:
            v = 1
        elif v == -1:
            kol += 1
            v = 0
            g = 0
            i -= 1
    elif a == 'D':
        if v == 0:
            v = -1
        elif v == 1:
            kol += 1
            v = 0
            g = 0
            i -= 1
    elif a == 'R':
        if g == 0:
            g = 1
        elif g == -1:
            kol += 1
            v = 0
            g = 0
            i -= 1
    else:
        if g == 0:
            g = -1
        elif g == 1:
            kol += 1
            v = 0
            g = 0
            i -= 1
    i += 1
print(kol + 1)

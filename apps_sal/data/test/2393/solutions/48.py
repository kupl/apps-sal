t = int(input())
for _ in range(t):
    poz = []
    x = input()
    i = 1
    d = len(x)
    while i < d - 1:
        q = x[i]
        if q == 'n':
            if x[i - 1] == 'o' and x[i + 1] == 'e':
                poz.append(i + 1)
        if q == 'w':
            if x[i - 1] == 't' and x[i + 1] == 'o':
                poz.append(i + 1)
        if i > 1 and i < d - 2 and q == 'o':
            if x[i - 2] == 't' and x[i + 2] == 'e' and x[i - 1] == 'w' and x[i + 1] == 'n':
                poz[-1] = i + 1
                i += 1
        i += 1
    print(len(poz))
    print(*poz)

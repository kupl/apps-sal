t = int(input())
for i in range(0, t):
    j = 0
    r = input()
    d = len(r)
    s = []
    while j < d - 2:
        if r[j] == 'o' and r[j + 1] == 'n' and r[j + 2] == 'e':
            s.append(j + 2)
            j += 3
        elif r[j] == 't' and r[j + 1] == 'w' and r[j + 2] == 'o':
            if j < d - 4 and r[j + 3] == 'n' and r[j + 4] == 'e':
                s.append(j + 3)
                j += 5
            else:
                s.append(j + 2)
                j += 3
        else:
            j += 1
    print(len(s))
    print(*s)



t = int(input())
for i in range(t):
    s = input()
    l = []
    if len(s) >= 3 and s[0] == 'o' and s[1] == 'n' and s[2] == 'e':
        l.append(2)
    elif len(s) >= 4 and s[1] == 'o' and s[2] == 'n' and s[3] == 'e':
        l.append(3)
    j = 2
    while j < len(s) - 2:
        if s[j] == 'o':
            if s[j-1] == 'w' and s[j-2] == 't':
                if s[j+1] == 'n' and s[j+2] == 'e':
                    l.append(j+1)
                else:
                    l.append(j)
            elif s[j+1] == 'n' and s[j+2] == 'e':
                l.append(j+2)
        j += 1
    if len(s) >= 3 and s[-3] == 't' and s[-2] == 'w' and s[-1] == 'o':
        l.append(len(s) - 1)
    elif len(s) >= 4 and s[-4] == 't' and s[-3] == 'w' and s[-2] == 'o':
        l.append(len(s) - 2)
    print(len(l))
    print(*l)


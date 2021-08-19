t = int(input())
for i in range(t):
    s = input()
    indexes = []
    j = 0
    while j < len(s) - 2:
        if s[j] == 'o' and s[j + 1] == 'n' and (s[j + 2] == 'e'):
            indexes.append(j + 1 + 1)
            j += 2
        elif s[j] == 't' and s[j + 1] == 'w' and (s[j + 2] == 'o'):
            if j + 3 < len(s) and s[j + 3] == 'n':
                indexes.append(j + 2 + 1)
                j += 3
            else:
                indexes.append(j + 1 + 1)
                j += 2
        j += 1
    print(len(indexes))
    print(*indexes)

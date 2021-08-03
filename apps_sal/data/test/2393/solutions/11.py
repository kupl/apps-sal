for i in range(int(input())):
    s = input()
    arr = []
    for j in range(len(s)):
        if s[j] == 'o':
            if j > 1 and j < len(s) - 2 and s[j + 1] == 'n' and s[j + 2] == 'e' and s[j - 1] == 'w' and s[j - 2] == 't':
                arr.append(j + 1)
            elif j > 1 and s[j - 1] == 'w' and s[j - 2] == 't' and (j == len(s) - 1 or s[j + 1] != 'o'):
                arr.append(j + 1)
            elif j > 1 and s[j - 1] == 'w' and s[j - 2] == 't' and j != len(s) - 1 and s[j + 1] == 'o':
                arr.append(j)
            elif j < len(s) - 2 and s[j + 1] == 'n' and s[j + 2] == 'e' and (j == 0 or s[j - 1] != 'o'):
                arr.append(j + 1)
            elif j < len(s) - 2 and s[j + 1] == 'n' and s[j + 2] == 'e' and j != 0 and s[j - 1] == 'o':
                arr.append(j + 2)
            '''if j > 1 and j < len(s) - 2 and s[j + 1] == 'n' and s[j + 2] == 'e' and s[j - 1] == 'w' and s[j - 2] == 't':
                arr.append(j + 1)
            elif j < len(s) - 2 and s[j + 1] == 'n' and s[j + 2] == 'e':
                arr.append(j + 1)
            elif j > 1 and s[j - 1] == 'w' and s[j - 2] == 't':
                arr.append(j + 1)'''
    print(len(arr))
    print(*arr)

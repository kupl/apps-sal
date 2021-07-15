for _ in range(int(input())):
    s = input()
    a = []
    i = 0
    while i <= (len(s) - 1):
        if s[i:i + 5] == 'twone':#and i + 4 >= len(s):
            a.append(i + 3)
            i += 5
        elif s[i] == 'o' and s[i:i + 3] == 'one':
            a.append(i + 2)
            i += 3
        elif s[i] == 't' and s[i:i + 3] == 'two':
            a.append(i + 2)
            i += 3
        else:
            i += 1
    print(len(a))
    if len(a) == 0:
        print('')
    else:
        print(*a)


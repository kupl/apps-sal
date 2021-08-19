t = int(input())
for j in range(0, t):
    i = 0
    s = input()
    res = []
    while i < len(s) - 2:
        if s[i] == 'o' and s[i + 1] == 'n' and s[i + 2] == 'e':
            res.append(i + 2)
            i += 3
        elif s[i] == 't' and s[i + 1] == 'w' and s[i + 2] == 'o':
            if i < len(s) - 4 and s[i + 3] == 'n' and s[i + 4] == 'e':
                # print(123123123)
                res.append(i + 3)
                i += 5
            else:
                res.append(i + 2)
                i += 3
        else:
            i += 1
    print(len(res))
    print(*res)

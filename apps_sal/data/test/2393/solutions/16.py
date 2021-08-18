for q in range(int(input())):
    s = input()
    ans = 0
    i = 0
    j = 0
    ans = []
    while i < (len(s) - 1):
        if i + 4 < len(s) and s[i: i + 5] == 'twone':
            ans.append(i + 3)
            i += 4
        elif i + 2 < len(s) and s[i: i + 3] == 'two':
            ans.append(i + 2)
            i += 2
        elif i + 2 < len(s) and s[i: i + 3] == 'one':
            ans.append(i + 2)
            i += 2
        i += 1
    print(len(ans))
    for e in ans:
        print(e, end=' ')
    print()

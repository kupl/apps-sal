for _ in range(int(input())):
    stro = list(input())
    ans = []
    for j in range(len(stro)):
        if j <= len(stro) - 5:
            if stro[j:j + 5] == ['t', 'w', 'o', 'n', 'e']:
                ans.append(j + 3)
                stro[j + 2] = '.'
        if j <= len(stro) - 3:
            if stro[j:j + 3] == ['t', 'w', 'o']:
                ans.append(j + 2)
                stro[j + 1] = '.'
        if j <= len(stro) - 3:
            if stro[j:j + 3] == ['o', 'n', 'e']:
                ans.append(j + 2)
                stro[j + 1] = '.'
    print(len(ans))
    print(*ans)

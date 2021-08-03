t = int(input())
for _ in range(t):
    s = input()
    i = 0
    ans = []
    n = len(s)
    while True:
        if i + 1 + 1 >= n:
            break
        if s[i] + s[i + 1] + s[i + 2] == 'one':
            ans.append(i + 1)
            i += 3
        elif s[i] + s[i + 1] + s[i + 2] == 'two':
            if i + 4 < n:
                if s[i + 2] + s[i + 3] + s[i + 4] == 'one':
                    ans.append(i + 2)
                    i += 5
                else:
                    ans.append(i + 1)
                    i += 3
            else:
                ans.append(i + 1)
                i += 3
        else:
            i += 1
    print(len(ans), sep='', end='')
    print()
    for i in ans:
        print(i + 1, sep='', end=' ')
    print()

t = int(input())
for i in range(t):
    cnt = 0
    a = []
    s = input()
    j = 0
    while j < len(s) - 2:
        if j < len(s) - 4 and s[j: j + 5] == 'twone':
            a.append(j + 2 + 1)
            cnt += 1
            j += 5
            continue
        elif s[j: j + 3] == 'one' or s[j: j + 3] == 'two':
            a.append(j + 1 + 1)
            cnt += 1
            j += 3
            continue
        j += 1
    print(cnt)
    print(*a)

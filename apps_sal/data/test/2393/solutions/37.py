t = int(input())
ans = []
for i in range(t):
    s = input()
    ans.append([])
    if len(s) > 2:
        j = 0
        while j < len(s) - 2:
            if j < len(s) - 4 and s[j:j + 5] == 'twone':
                ans[-1].append(j + 3)
                j += 4
            elif s[j:j + 3] == 'two':
                ans[-1].append(j + 2)
                j += 1
            elif s[j:j + 3] == 'one':
                ans[-1].append(j + 2)
                j += 1
            else:
                j += 1
for i in ans:
    print(len(i))
    print(*i)

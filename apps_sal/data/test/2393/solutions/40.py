t = int(input())
for _ in range(t):
    s = input()
    len_s = len(s)
    ans = [0, []]
    for i in range(len_s):
        if s[i] == 'o':
            if i >= 2 and s[i - 1] == 'w' and (s[i - 2] == 't') and (i + 2 < len_s) and (s[i + 1] == 'n') and (s[i + 2] == 'e'):
                ans[0] += 1
                ans[1].append(i + 1)
            elif i >= 2 and s[i - 1] == 'w' and (s[i - 2] == 't'):
                ans[0] += 1
                ans[1].append(i)
            elif i + 2 < len_s and s[i + 1] == 'n' and (s[i + 2] == 'e'):
                ans[0] += 1
                ans[1].append(i + 2)
    print(ans[0])
    print(*ans[1])

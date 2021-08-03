s = list(input())

ans = {'R': 0, 'B': 0, 'Y': 0, 'G': 0}


for i, ch in enumerate(s):
    if ch != '!':
        for j in range(i, len(s), 4):
            if s[j] == '!':
                s[j] = ch
                ans[ch] += 1
        for j in range(i, -1, -4):
            if s[j] == '!':
                s[j] = ch
                ans[ch] += 1

print(ans['R'], ans['B'], ans['Y'], ans['G'])

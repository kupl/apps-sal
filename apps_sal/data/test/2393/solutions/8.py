t = int(input())
for i in range(t):
    s = list(input())
    ans = []
    for i in range(len(s) - 4):
        if s[i:i + 5] == ['t', 'w', 'o', 'n', 'e']:
            ans.append(i + 3)
            s[i + 2] = 'q'
    for i in range(len(s) - 2):
        if s[i:i + 3] == ['o', 'n', 'e'] or s[i:i + 3] == ['t', 'w', 'o']:
            ans.append(i + 2)
            s[i + 1] = 'q'
    print(len(ans))
    print(' '.join(map(str, ans)))

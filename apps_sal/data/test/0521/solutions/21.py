n = int(input())
s = input()
s = '*' + s
s += '#'
yes = 0
if s[1] == '?' or s[n] == '?':
    yes = 1
for i in range(1, n + 2 - 1):
    if s[i] == '?':
        if (s[i - 1] != s[i + 1]) == False or s[i - 1] == '?' or s[i + 1] == '?':
            yes = 1
    elif s[i] == s[i - 1]:
        print('No')
        break
else:
    if yes:
        print('Yes')
    else:
        print('No')

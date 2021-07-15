n = int(input())
s = list(input())
for i in range(n - 1):
    if s[i] == 'U' and s[i + 1] == 'R':
        s[i] = 'D'
        s[i + 1] = ''
    if s[i] == 'R' and s[i + 1] == 'U':
        s[i] = 'D'
        s[i + 1] = ''
print(len(''.join(s)))


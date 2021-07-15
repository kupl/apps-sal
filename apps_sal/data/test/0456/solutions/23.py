n, s = int(input()), input()
s, ans = s + 'ii', []
i = 0
while i < n:
    if s[i] == 'o' and s[i + 1] == 'g' and s[i + 2] == 'o':
        i += 3
        while i < n and s[i] == 'g' and s[i + 1] == 'o':
            i += 2
        ans.append('***')
    else:
        ans.append(s[i])
        i += 1
print(''.join(ans))

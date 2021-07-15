s = input()
for i in range(len(s)):
    if i % 2 == 0:
        if s[i] == 'L':
            print('No')
            return
    else:
        if s[i] == 'R':
            print('No')
            return
print('Yes')


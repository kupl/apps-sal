s = input()
count = 0
for i in range(0, len(s)):
    if i % 2 == 0 and s[i] == 'L':
        print('No')
        count = 1
        break
    elif i % 2 == 1 and s[i] == 'R':
        print('No')
        count = 1
        break
if count == 0:
    print('Yes')

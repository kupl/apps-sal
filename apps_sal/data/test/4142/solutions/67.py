s = input()
bool = True
for i in range(len(s)):
    if i % 2 == 0:
        if s[i] != 'R' and s[i] != 'U' and s[i] != 'D':
            bool = False
    else:
        if s[i] != 'L' and s[i] != 'U' and s[i] != 'D':
            bool = False
if bool:
    print('Yes')
else:
    print('No')

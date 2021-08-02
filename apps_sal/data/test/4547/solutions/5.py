# 93
s = list(input())
c = 0
for i in range(0, len(s)):
    if s[i] == '9':
        c = c + 1
if c == 0:
    print('No')
else:
    print('Yes')

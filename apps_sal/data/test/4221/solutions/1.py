s = list(input())
if s[-1] == 's':
    s.append('e')
    s.append('s')
else:
    s.append('s')
for i in range(len(s)):
    print(s[i], end='')

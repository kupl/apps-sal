s = input()
s2 = 'CODEFORCES'
while s and s2 and (s[0] == s2[0]):
    s = s[1:]
    s2 = s2[1:]
while s and s2 and (s[-1] == s2[-1]):
    s = s[:-1]
    s2 = s2[:-1]
if s2 == '':
    print('YES')
else:
    print('NO')

s = str(input())

if s[0] == 'A':
    t = 'B'
else:
    t = 'A'

answer = s.find(t)

if answer != -1:
    print('Yes')
else:
    print('No')

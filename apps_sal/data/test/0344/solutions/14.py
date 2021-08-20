s = input()
flag = True
g = ['a', 'o', 'u', 'i', 'e']
for i in range(len(s) - 1):
    if s[i] is not 'n' and s[i] not in g and (s[i + 1] not in g):
        flag = False
if s[-1] not in g and s[-1] is not 'n':
    flag = False
if flag:
    print('YES')
else:
    print('NO')

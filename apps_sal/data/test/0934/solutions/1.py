s = input()
d = input().split()
f = False
for i in d:
    if i[0] == s[0] or i[1] == s[1]:
        f = True
        break
if f:
    print('YES')
else:
    print('NO')

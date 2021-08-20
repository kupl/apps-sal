n = int(input())
s = input()
pr = True
for i in range(len(s)):
    if s[i] in '3690':
        pr = False
vn = True
for i in range(len(s)):
    if s[i] in '709':
        vn = False
le = True
for i in range(len(s)):
    if s[i] in '1470':
        le = False
vv = True
for i in range(len(s)):
    if s[i] in '123':
        vv = False
if pr or vn or le or vv:
    print('NO')
else:
    print('YES')

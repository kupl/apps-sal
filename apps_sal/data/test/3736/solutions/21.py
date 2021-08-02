s = input()
k = 'AHIMOTUVWXY'
r = True
for c in s:
    r &= c in k
    if not r: break
if r and s == s[::-1]:
    print('YES')
else:
    print('NO')

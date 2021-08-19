s = input().strip()
fl = True
for i in s:
    if i not in 'AHIMOTUVWXY':
        fl = False
        break
if s == s[::-1] and fl:
    print('YES')
else:
    print('NO')

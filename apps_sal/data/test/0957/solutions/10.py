s = input()
pt = 'heidi'
i = 0
for v in s:
    if i < 5 and v == pt[i]:
        i += 1
if i == 5:
    print('YES')
else:
    print('NO')

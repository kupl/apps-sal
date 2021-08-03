neats = 'AEFHIKLMNTVWXYZ'
s = input()
un, n = 0, 0
for c in s:
    if c not in neats:
        un += 1
    else:
        n += 1
print('YES' if un == 0 or n == 0 else 'NO')

s = input()
i = 0
ab = False
ba = False
o = 0
while i < len(s) - 1:
    if i < len(s) - 2 and (not o and not ab and not ba) and (s[i:i + 2] == 'AB' and s[i + 1:i + 3] == 'BA') or (s[i:i + 2] == 'BA' and (s[i + 1:i + 3] == 'AB')):
        o += 1
        i += 2
    elif s[i:i + 2] == 'AB' and not ab:
        ab = True
        i += 1
    elif s[i:i + 2] == 'BA' and not ba:
        ba = True
        i += 1
    i += 1
if ab + ba + o >= 2:
    print('YES')
else:
    print('NO')

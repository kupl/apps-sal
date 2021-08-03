s = input().rstrip()
good = '14'
for j in s:
    if j not in good:
        print('NO')
        return
cur = ''
for i in range(len(s)):
    if s[i] == '1':
        cur = '1'
    else:
        cur += '4'
        if cur == '14' and i != len(s) - 1 and s[i + 1] == '4':
            continue
        if cur != '14' and cur != '144':
            print('NO')
            return
        else:
            cur = ''
print('YES')

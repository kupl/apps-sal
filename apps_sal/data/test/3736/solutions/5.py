good = ['A', 'H', 'I', 'M', 'O', 'T', 'U', 'W', 'V', 'X', 'Y']
s = input().strip()
f = 1
for i in range(len(s)):
    if s[i] not in good:
        f = 0
if f and s == s[::-1]:
    print('YES')
else:
    print('NO')

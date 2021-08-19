l = ['A', 'H', 'I', 'M', 'O', 'T', 'U', 'V', 'W', 'X', 'Y']
s = input()
if s == s[::-1] and len(set(s) | set(l)) == len(l):
    print('YES')
else:
    print('NO')

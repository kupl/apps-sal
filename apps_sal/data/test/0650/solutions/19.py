l = ['A', 'E', 'F', 'H', 'I', 'K', 'L', 'M', 'N', 'T', 'V', 'W', 'X', 'Y', 'Z']
s = input()
a = 0
for i in s:
    if i in l:
        a += 1
if a == len(s) or a == 0:
    print('YES')
else:
    print('NO')

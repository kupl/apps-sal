curved = 'QRUOPJGDSCB'
s = input()
ctr = 0
for i in s:
    if i in curved:
        ctr += 1
if ctr == 0 or ctr == len(s):
    print('YES')
else:
    print('NO')

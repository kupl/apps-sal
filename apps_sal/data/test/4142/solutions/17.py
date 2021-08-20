s = input()
ok = 0
for i in range(len(s)):
    if i % 2 == 0 and s[i] == 'L':
        ok += 1
    if i % 2 == 1 and s[i] == 'R':
        ok += 1
if ok == 0:
    print('Yes')
else:
    print('No')

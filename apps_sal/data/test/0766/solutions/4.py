s = input()
kol = 0
for i in range(26):
    if chr(i + 97) in s:
        kol += 1
tmp = list(set(s))
if kol == 4:
    print('Yes')
elif kol == 3 and len(s) != 3:
    print('Yes')
elif kol == 2 and s.count(tmp[0]) != 1 and (s.count(tmp[1]) != 1):
    print('Yes')
else:
    print('No')

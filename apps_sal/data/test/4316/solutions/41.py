s = input()

cou = []
enc = 0
enc1 = 0
for i in s:
    if i not in cou:
        cou.append(i)

if len(cou) != 2:
    print('No')
    return

for i in s:
    if i in cou[0]:
        enc += 1
    if i in cou[1]:
        enc1 += 1

if enc == 2 and enc1 == 2:
    print('Yes')
else:
    print('No')

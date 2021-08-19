import re
inputstr = input()
strlen = len(inputstr)
ab = []
ba = []
for m in re.finditer('AB', inputstr):
    ab.append([m.start(), m.end() - 1])
for m in re.finditer('BA', inputstr):
    ba.append([m.start(), m.end() - 1])
found = False
for i in range(len(ab)):
    for j in range(len(ba)):
        if ab[i][0] != ba[j][0] and ab[i][0] != ba[j][1] and (ab[i][1] != ba[j][0]) and (ab[i][1] != ba[j][1]):
            found = True
            break
    if found:
        break
if found:
    print('YES')
else:
    print('NO')

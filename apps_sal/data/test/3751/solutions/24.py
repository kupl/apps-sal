s = input()
idents = list('abcdefghijklmnopqrstuvwxyz')
possible = True
for x in s:
    if not idents:
        break
    elif x == idents[0]:
        idents.pop(0)
    elif x not in idents:
        continue
    else:
        possible = False
print('YES' if possible else 'NO')


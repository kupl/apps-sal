s = input()
fin = ''
for c in s:
    if c == '1':
        fin += '1'
    elif c == '0':
        fin += '0'
    elif len(fin) > 0:
        fin = fin[:-1]
print(fin)

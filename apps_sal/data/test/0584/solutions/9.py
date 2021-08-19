n = int(input())
s = input()
out = []
inn = []
p = ''
for x in s:
    if x == '(':
        out.append(p)
        p = ''
    elif x == ')':
        inn.append(p)
        p = ''
    else:
        p += x
out.append(p)
oouut = []
for x in out:
    for y in x.split('_'):
        if len(y):
            oouut.append(y)
iiinn = []
for x in inn:
    for y in x.split('_'):
        if len(y):
            iiinn.append(y)
max = 0
for k in oouut:
    if len(k) > max:
        max = len(k)
print(max, len(iiinn))

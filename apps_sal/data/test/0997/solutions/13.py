b = []


def check(x):
    if '.' in x:
        return False
    if x == '0':
        return True
    if x == '':
        return False
    if x[0] == '0':
        return False
    for i in x:
        if i not in '1234567890':
            return False
    return True


s = input()
k = ''
for i in s:
    if i == ';':
        k += ','
    else:
        k += i

kk = k.split(',')
a = []
for i in kk:
    if check(i):
        a.append(i)
    else:
        b.append(i)

if a == []:
    print("-")
else:
    print('"' + ','.join(a) + '"')

if b == []:
    print("-")
else:
    print('"' + ','.join(b) + '"')

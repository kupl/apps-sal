def compare(a, b):
    fl = True
    if len(a) > len(b):
        return True
    elif len(a) < len(b):
        return False
    elif len(a) == len(b):
        fl = None
        for i in range(len(a)):
            if int(b[i]) > int(a[i]) and fl == None:
                fl = False
                break
            elif int(a[i]) > int(b[i]) and fl == None:
                fl = True
                break
        if fl == None:
            fl = True
        return fl


n = input()
l = []
a = ''
i = 0
while i < len(n):
    a += n[i]
    fl = False
    while i < len(n) and n[i] == '0':
        l[-1] += '0'
        i += 1
        fl = True
    if fl:
        a = ''
        continue
    l.append(a)
    i += 1
    a = ''
s = 1
for i in list(range(1, len(l))):
    if compare(l[i - 1], l[i]):
        s = s + 1
    else:
        s = 1
    l[i] = l[i - 1] + l[i]
    l[i - 1] = ''
print(s)

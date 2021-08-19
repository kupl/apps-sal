q = input()
a = []
w = len(q)
i = w - 1
while i > 0:
    if '0' <= q[i] <= '9':
        j = i - 1
        while not 'a' <= q[j] <= 'z':
            j -= 1
        a.append(q[j + 1:i + 1])
        i = j
    i -= 1
s = 0
for i in a:
    l = len(i)
    if l > 2:
        if i[l - 3] == '.':
            s += int(i[l - 2:])
            i = i[:l - 3]
        i = i.replace('.', '')
    s += int(i) * 100
d = ''
r = s
if s % 100 != 0:
    d = '.' + str(s % 100)
if len(d) == 2:
    d = d[0] + '0' + d[1]
s //= 100
rt = s
tr = d
while s // 1000 != 0:
    t = str(s % 1000)
    if len(t) == 1:
        t = '.00' + t
    elif len(t) == 2:
        t = '.0' + t
    else:
        t = '.' + t
    d = t + d
    s //= 1000
if s != 0:
    t = str(s % 1000)
    d = t + d
else:
    d = d[1:]
if len(d) == 2:
    d = '0.' + d
elif d == '':
    d = '0'
print(d)

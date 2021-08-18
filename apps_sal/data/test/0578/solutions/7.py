s = input()
a, s = s.split('.')
d, b = s.split('e')
for i in range(int(b)):
    d += '0'
    a += d[0]
    d = d[1:]
s = a + '.' + d
while s[0] == '0':
    s = s[1:]
while s[-1] == '0':
    s = s[:-1]
if s[-1] == '.':
    s = s[:-1]
if s == '' or s[0] == '.':
    s = '0' + s
print(s)

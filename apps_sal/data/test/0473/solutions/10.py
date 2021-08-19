s = input().split(':')
t = input().split(':')
h = int(s[0]) - int(t[0])
m = int(s[1]) - int(t[1])
while m < 0:
    m += 60
    h -= 1
while h < 0:
    h += 24
mstr = ''
if m < 10:
    mstr = '0' + str(m)
else:
    mstr = str(m)
hstr = ''
if h < 10:
    hstr = '0' + str(h)
else:
    hstr = str(h)
print(hstr + ':' + mstr)

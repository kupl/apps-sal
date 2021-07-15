s = input()
a = s[0]
s = s[2:]
b = s[:s.find('e')]
d = int(s[s.find('e') + 1:])

s = ''

if d < 0:
    s = '0.' + a
    d -= 1
    s += '0' * -d
    d = 0
    s += b

else:
    s = a
    while d > 0:
        s += b[0]
        b = b[1:] + '0'
        d -= 1
    s += '.' + b

while len(s) and s[0] == '0':
    s = s[1:]
s = s[::-1]
while len(s) and s[0] == '0':
    s = s[1:]
s = s[::-1]

if s[0] == '.':
    s = '0' + s

if s[-1] == '.':
    s = s[:-1]

print(s)


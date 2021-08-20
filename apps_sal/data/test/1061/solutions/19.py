a = input().split(' ')
b = input().split(' ')
c = input().split(' ')
d = input().split(' ')
e = input().split(' ')
x = 0
y = 0
if '1' in a:
    y = a.index('1')
    x = 0
if '1' in b:
    y = b.index('1')
    x = 1
if '1' in c:
    y = c.index('1')
    x = 2
if '1' in d:
    y = d.index('1')
    x = 3
if '1' in e:
    y = e.index('1')
    x = 4
print(abs(x - 2) + abs(y - 2))

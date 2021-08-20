n = input()
s = input()
a = b = 0
for c in s:
    if c == '1':
        a += 1
    else:
        b += 1
if a != b:
    print(1)
    print(s)
else:
    print(2)
    print('{} {}'.format(s[:-1], s[-1]))

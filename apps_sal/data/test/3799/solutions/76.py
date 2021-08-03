s = input().strip()
c1, c2 = s[0], s[-1]
if c1 == c2:
    if len(s) % 2:
        print('Second')
    else:
        print('First')
else:
    if len(s) % 2:
        print('First')
    else:
        print('Second')

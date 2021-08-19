s = input().strip()
l = len(s)
if (l + (s[0] == s[-1])) % 2:
    print('First')
else:
    print('Second')

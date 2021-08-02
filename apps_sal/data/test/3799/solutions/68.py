s = input()
if (len(s) + (s[0] == s[-1])) % 2 == 1:
    print('First')
else:
    print('Second')

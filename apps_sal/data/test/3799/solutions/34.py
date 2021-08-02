s = input()

if (len(s) % 2 == 1 and s[-1] != s[0]) or (len(s) % 2 == 0 and s[-1] == s[0]):
    print('First')
else:
    print('Second')

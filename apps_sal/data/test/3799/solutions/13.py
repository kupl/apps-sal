s = input()
if len(s) % 2 == 0 and s[0] == s[-1]:
    print('First')
elif len(s) % 2 == 0 or s[0] == s[-1]:
    print('Second')
else:
    print('First')

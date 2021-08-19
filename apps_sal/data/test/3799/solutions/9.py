s = input()
if s[0] == s[len(s) - 1]:
    if len(s) % 2 == 1:
        print('Second')
    else:
        print('First')
elif len(s) % 2 == 1:
    print('First')
else:
    print('Second')

s = input()
if s[0] == s[len(s) - 1]:
    a = len(s) - 3
else:
    a = len(s) - 2
if a % 2 == 0:
    print('Second')
else:
    print('First')

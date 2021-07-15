s = input()
ans = len(s) & 1
if (s[0] == s[-1]) ^ ans:
    print('First')
else:
    print('Second')



s = list((input() for i in range(2)))
if s[0] == s[1][:-1]:
    print('Yes')
else:
    print('No')

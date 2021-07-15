s = input()
if s[s.find('1'):].count('0') >= 6:
    print('yes')
else:
    print('no')

s = input()
one = s.find('1')
if one == -1:
    print('no')
else:
    s = s[one:]
    zero = s.count('0')
    if zero >= 6:
        print('yes')
    else:
        print('no')

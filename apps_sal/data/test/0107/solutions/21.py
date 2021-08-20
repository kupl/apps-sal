n = input()
if '1' in n:
    n = n[n.find('1'):]
    if n.count('0') >= 6:
        print('yes')
    else:
        print('no')
else:
    print('no')

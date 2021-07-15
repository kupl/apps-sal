s = input()
if s.count('ABC') + s.count('ACB') + s.count('BAC') + s.count('BCA') + s.count('CAB') + s.count('CBA') != 0:
    print('Yes')
else:
    print('No')

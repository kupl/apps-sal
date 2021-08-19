p = input()
if p == '0':
    print('Yes')
elif len(p) == 1 and p != '9':
    print('No')
elif len(p) == 1 and p == '9':
    print('Yes')
elif sum([int(val) for val in p]) % 9 == 0:
    print('Yes')
else:
    print('No')

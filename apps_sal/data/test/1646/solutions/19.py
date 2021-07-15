_ = input()
s = input()

ones = len([i for i in s if i == '1'])
zeros = len([i for i in s if i == '0'])

if ones == 0:
    print('0')
else:
    print('1' + '0' * zeros)



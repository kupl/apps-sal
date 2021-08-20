a = int(input())
b = a // 100
c = a // 10
c = c % 10
d = a
d = d % 10
if b ^ c ^ d:
    print('Inclusive')
else:
    print('Exclusive')

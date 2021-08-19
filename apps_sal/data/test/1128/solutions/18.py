y = input('').split(' ')
a = int(y[0])
m = int(y[1])
while m % 2 == 0:
    m = m / 2
if a % m == 0:
    print('Yes')
else:
    print('No')

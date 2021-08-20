numline = input().split(' ')
a = int(numline[0])
b = int(numline[1])
if 2 * a <= b and b <= 4 * a and (b % 2 == 0):
    print('Yes')
else:
    print('No')

(a, b) = (int(x) for x in input().split(' '))
turns = min(a, b) - 1
if turns % 2 == 0:
    print('Akshat')
else:
    print('Malvika')

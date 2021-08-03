s = input()
k1 = s.count('x')
k2 = s.count('y')
if k1 > k2:
    print('x' * (k1 - k2))
else:
    print('y' * (k2 - k1))

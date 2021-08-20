s = input()
x = s.count('x')
y = s.count('y')
if x > y:
    print('x' * (x - y))
else:
    print('y' * (y - x))

a = input()
x = a.count('x')
y = a.count('y')
if x > y:
    print('x' * (x - y))
else:
    print('y' * (y - x))

l = list(input())
x = l.count('x')
y = l.count('y')
print('x' * (x - y) if x > y else 'y' * (y - x))

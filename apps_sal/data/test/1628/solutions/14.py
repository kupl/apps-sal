s = input()
(x, y) = (s.count('x'), s.count('y'))
if x > y:
    print('x' * (x - y))
else:
    print('y' * (y - x))

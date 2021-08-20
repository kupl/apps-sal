s = input()
a = s.count('x')
b = s.count('y')
if a > b:
    s = 'x' * (a - b)
else:
    s = 'y' * (b - a)
print(s)

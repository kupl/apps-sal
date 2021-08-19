var = input('')
var = var.split(' ')
x = int(var[0])
y = int(var[1])
if x == 1 and y == 1:
    print('1')
else:
    p1 = (y - 1) / (x * y - 1)
    p2 = (1 - p1) * (1 / x)
    print(p1 + p2)

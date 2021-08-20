string = input()
numbers = string.split(' ')
a = int(numbers[0])
b = int(numbers[1])
x = a // 2 // (b + 1)
y = b * x
z = a - x - y
print('%d %d %d' % (x, y, z))

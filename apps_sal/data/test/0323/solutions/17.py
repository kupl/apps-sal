import math
string = input()
numbers = string.split(' ')
a = int(numbers[0])
b = int(numbers[1])
print(math.factorial(min([a, b])))

string = input()
numbers = string.split()
a, b = int(numbers[0]), int(numbers[1])
n = a // b
if n % 2 == 1:
    print("YES")
else:
    print("NO")

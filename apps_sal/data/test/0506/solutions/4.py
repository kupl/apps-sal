a, b = list(map(int, str.split(input())))
count = 0
while a and b:

    a, b, count = b, a % b, count + a // b

print(count)

number, iterations = [int(x) for x in input().strip().split(' ')]
for i in range(iterations):
    if number % 10 == 0:
        number = number // 10
    else:
        number -= 1

print(number)

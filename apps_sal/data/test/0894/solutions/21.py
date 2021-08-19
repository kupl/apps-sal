number = input('')
for index in range(0, len(number)):
    if number[index] == ' ':
        split = index
num1 = number[0:split]
num2 = number[split:len(number)]
num1 = int(num1)
num2 = int(num2)
sum = abs(num1) + abs(num2)
if num1 > 0 and num2 > 0:
    print(0, sum, sum, 0)
if num1 < 0 and num2 > 0:
    print(-1 * sum, 0, 0, sum)
if num1 > 0 and num2 < 0:
    print(0, -sum, sum, 0)
if num1 < 0 and num2 < 0:
    print(-sum, 0, 0, -sum)

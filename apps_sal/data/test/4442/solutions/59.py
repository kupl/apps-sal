input_line = input().rstrip().split()
num1 = int(input_line[0])
num2 = int(input_line[1])

if (num1 > num2):
    print(str(num2) * num1)
elif (num1 < num2):
    print(str(num1) * num2)
elif (num1 == num2):
    print(str(num1) * num2)

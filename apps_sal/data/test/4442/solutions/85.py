num, num1 = input("").split()
num = int(num)
num1 = int(num1)

if num <= num1:
    for i in range(num1):
        print(num, end='')
else:
    for i in range(num):
        print(num1, end='')

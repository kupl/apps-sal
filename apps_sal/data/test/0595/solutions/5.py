n = int(input())
num = 0
if n % 400 == 0 or (n % 4 == 0 and n % 100 != 0):
    num = 1
n2 = n + 1
num2 = 365 + num
while True:
    num3 = 0
    if n2 % 400 == 0 or (n2 % 4 == 0 and n2 % 100 != 0):
        num3 = 1
    if num2 % 7 == 0:
        if num3 == num:
            break
    num2 += 365 + num3
    n2 += 1
print(n2)


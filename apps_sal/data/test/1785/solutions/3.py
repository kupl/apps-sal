n = int(input())
s = input()
num = s.count('A')
num1 = s.count('C')
num2 = s.count('T')
num3 = s.count('G')
num4 = max(num, num1, num2, num3)
num5 = 0
if num == num4:
    num5 += 1
if num1 == num4:
    num5 += 1
if num2 == num4:
    num5 += 1
if num3 == num4:
    num5 += 1
if num5 == 1 or n == 1:
    print(1)
else:
    print(num5 ** n % (10 ** 9 + 7))

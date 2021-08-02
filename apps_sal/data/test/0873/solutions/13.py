n = int(input())
num = input()
num2 = input()
num3 = 0
for i in range(n):
    temp = abs(int(num[i]) - int(num2[i]))
    num3 += min(temp, 10 - temp)
print(num3)

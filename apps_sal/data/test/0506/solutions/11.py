a, b = list(map(int, input().split()))
num = 0
while b > 0:
    temp = b
    num += (a // b)
    b = a % b
    a = temp
print(num)

a = input()
b = input()
al = len(a)
bl = len(b)
num = bl - al + 1
num2 = 0
for i in range(num):
    if a[0] != b[i]:
        num2 += 1
num3 = num2
for i in range(1, al):
    if a[i - 1] != a[i]:
        if a[i] == b[i - 1]:
            num2 -= 1
        num2 = num - num2 - 1
    elif a[i] != b[i - 1]:
        num2 -= 1
    if a[i] != b[i + num - 1]:
        num2 += 1
    num3 += num2
print(num3)

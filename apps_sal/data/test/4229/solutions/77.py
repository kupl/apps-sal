n = int(input())
num = 0
for i in range(1, n + 1):
    if i % 3 == 0:
        continue
    elif i % 5 == 0:
        continue
    else:
        num += i
print(num)

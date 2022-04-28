number = int(input())
replacement = [16, 2, 8, 4, 1, 32]
result = 0
for k in range(6):
    if number % 2 == 1:
        result += replacement[k]
        number -= 1
    number /= 2
print(result)

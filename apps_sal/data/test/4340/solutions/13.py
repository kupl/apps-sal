length = int(input())
numbers = list(map(int, input().split(' ')))
for i in range(length):
    if numbers[i] % 2 == 0:
        numbers[i] -= 1
res = ''
for i in numbers:
    res += str(i) + ' '
print(res.strip())

n = int(input())
b = [0] * n
sum = 0
i = 0
for s in input().split():
    sum += int(s) - 1
    b[i] = sum
    i += 1
for i in range(n):
    print(2 - b[i] % 2)

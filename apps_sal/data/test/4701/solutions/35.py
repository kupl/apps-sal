n, k = [int(input()) for i in range(2)]

number = 1

for i in range(n):
    number = min(2 * number, number + k)
print(number)

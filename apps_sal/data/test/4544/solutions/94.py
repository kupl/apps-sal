n = int(input())
numbers = list(map(int, input().split()))
number_colle = [0] * (10 ** 5 + 2)
for i in range(n):
    choise = numbers[i] + 1
    for j in [-1, 0, 1]:
        number_colle[choise + j] += 1
print(max(number_colle))

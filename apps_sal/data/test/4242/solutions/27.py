import math
(num1, num2, target) = list(map(int, input().split()))
number = math.gcd(num1, num2)
table = []
for j in range(1, number + 1):
    if number % j == 0:
        table.append(j)
list.sort(table, reverse=True)
print(table[target - 1])

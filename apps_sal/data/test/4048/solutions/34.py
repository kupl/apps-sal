import math
n = int(input())
List = []
n_sqrt = int(math.sqrt(n))
for i in range(1, n_sqrt + 1):
    if n % i == 0:
        number = i + n // i - 2
        List.append(number)
print(min(List))

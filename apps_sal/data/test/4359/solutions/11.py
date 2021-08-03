import math

dishes = []
rest = 10

for i in range(5):
    n = int(input())
    dishes.append(math.ceil(n / 10) * 10)
    if 0 < n % 100 % 10 < rest:
        rest = n % 100 % 10

print(sum(dishes) - (10 - rest))

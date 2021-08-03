import math
x = int(input())
# x = 10**15
xi = math.floor(x / 5.5)
# print(xi)
for i in range(xi, 10000000000000000000000000000):
    # print(6*i - math.floor(i/2))
    if(x <= 6 * i - math.floor(i / 2)):
        xa = i
        break

print(xa)

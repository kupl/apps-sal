import math
n, r = list(map(int, input().split(' ')))
l = 2 * r * math.sin(math.pi / n)
R = l * r / (-l + 2 * r)
print(R)

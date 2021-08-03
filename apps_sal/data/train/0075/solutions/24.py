import math
PI = math.pi


def radius(n):
    return 0.5 / math.sin(PI / (2 * n))


def chord(num_sides, n):
    return 2 * radius(n) * math.sin((PI * num_sides) / (2 * n))


t = int(input())

for i in range(t):
    n = int(input())
    x = int(n / 2) + 1
    y = int(n / 2)
    print(chord(x, n) / math.sqrt(2) + chord(y, n) / math.sqrt(2))

import math
n, r = list(map(int, input().split()))
a = math.pi / n
b = a / 2
print(r * math.sin(b) / math.sin(math.pi - a - b) * math.sin(a) * r * n)
                               


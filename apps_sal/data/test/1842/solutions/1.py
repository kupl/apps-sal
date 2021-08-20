import math
(a, b, c) = list(map(int, input().split()))
D = math.sqrt(b * b - 4 * a * c)
x1 = (-b + D) / (2 * a)
x2 = (-b - D) / (2 * a)
if D == 0:
    print(max(x1, x2))
else:
    print(max(x1, x2))
    print(min(x1, x2))

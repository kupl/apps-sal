import math
t = int(input())
while t > 0:
    (n, b) = map(int, input().split())
    tobemade = math.ceil((n * (b - 1) + 1) / b)
    print(tobemade)
    t -= 1

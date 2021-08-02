import math
for _ in range(int(input())):
    x, y = map(int, input().split())
    if x < 3:
        print(1)
    else:
        x -= 2
        x = math.ceil(x / y)
        print(x + 1)

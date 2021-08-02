import math
for _ in range(int(input())):
    a, b, c, d = list(map(int, input().split()))
    need = a - b
    if (need <= 0):
        print(b)
    else:
        if (c - d) <= 0:
            print(-1)
        else:
            print(b + math.ceil((need / (c - d))) * c)

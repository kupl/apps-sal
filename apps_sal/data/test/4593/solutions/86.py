import math


def resolve():
    x = int(input())
    sqrt_x = int(math.sqrt(x))
    al = list()
    for i in range(2, 10):
        for j in range(sqrt_x, 0, -1):
            if j**i <= x:
                al.append(j**i)
                break
    al = sorted(al)
    print(al[-1])


resolve()

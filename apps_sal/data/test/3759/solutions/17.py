from math import sqrt, floor


def calc(n):
    if n == 0:
       return 1

    # y = n
    # x = 1
    # c = 0
    # while x - y < 0:
    #     if x ** 2 + y ** 2 <= n ** 2:
    #         c += 1
    #         x += 1
    #         continue
    #     if x ** 2 + y ** 2 > n ** 2:
    #         y -= 1
    x = floor(sqrt(n**2/2))
    y = floor(sqrt(n**2-x**2))
    #print(x, y)
    if x == y:
        return x*8
    else:
        return x * 8 +4

n = int(input())
print(calc(n))

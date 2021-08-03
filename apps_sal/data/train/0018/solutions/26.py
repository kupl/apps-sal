import math


def main():
    n = int(input())
    a = math.pi / (2 * n)
    x = 1 / (math.sin(a)) / 2
    res = 2 * math.cos(a) * x
    print(res)


for _ in range(int(input())):
    main()

from math import ceil as cc


def mi():
    return map(int, input().split())


'\n5\n2 3\n10 10\n2 4\n7 4\n9 3\n'
n = int(input())
for i in range(n):
    (a, b) = mi()
    if a == b:
        print(0)
    elif (b - a) % 2 == 0 and b > a:
        print(2)
    elif (b - a) % 2 and b > a:
        print(1)
    elif (b - a) % 2 == 0 and b < a:
        print(1)
    else:
        print(2)

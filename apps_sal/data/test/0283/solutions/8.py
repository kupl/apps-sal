n = int(input())


def yes(x):
    if (x < 3):
        return 0
    else:
        for y in range(2, x):
            if (x % y == 0):
                return 1
        return 0


for m in range(1, 1001):
    if yes(n * m + 1):
        print(m)
        break

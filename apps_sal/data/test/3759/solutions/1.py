import math
import fileinput

for line in fileinput.input():
    n = int(line)


def countPoints(n):
    if n == 0:
        return 1
    elif n == 1:
        return 4
    else:
        X = math.floor(math.sqrt(2) / 2 * n)
        if (X**2 + (X + 1)**2 <= n**2):
            return 8 * X + 4
        else:
            return 8 * X


print(countPoints(n))

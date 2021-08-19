import math
(a, b, c, d) = map(int, input().split())
x = math.ceil(a / d)
z = math.ceil(c / b)


def result():
    if x >= z:
        return 'Yes'
    else:
        return 'No'


print(result())

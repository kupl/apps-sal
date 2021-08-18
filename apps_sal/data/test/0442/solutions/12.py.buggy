from math import sqrt, ceil
r = int(input())
def func(x): return (r - 1 - x - x * x) / 2 / x


for x in range(1, ceil(sqrt(r)) + 1):
    y = func(x)
    if y > 0 and y == int(y):
        print(x, int(y))
        return
print('NO')

from math import gcd


def lcm(x, y):
    return (x * y) // gcd(x, y)


def arr_lcm(arr):
    if len(arr) == 2:
        return lcm(arr[0], arr[1])
    return lcm(arr[0], arr_lcm(arr[1:]))


n = int(input())
print(arr_lcm([i for i in range(1, n + 1)]) + 1)

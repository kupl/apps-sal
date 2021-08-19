def ceil(x):
    if x - int(x) == 0:
        return int(x)
    return int(x + 1)


(n, x, t) = [int(x) for x in input().split()]
print(ceil(n / x) * t)

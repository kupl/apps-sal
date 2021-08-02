def f(a, b):
    if a % b > 0:
        return int(a / b) + f(b, a % b)
    return int(a / b)


a, b = list(map(int, input().split()))
print(f(a, b))

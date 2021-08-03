a, b = map(int, input().split())


def f(a, b):
    if a == b:
        return 1
    elif a == 0 or b == 0:
        return 0
    else:
        return a // b + f(max(a - b * (a // b), b), min(a - b * (a // b), b))


print(f(a, b))

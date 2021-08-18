a, b = map(int, input().split())


def solve(x):
    if x % 4 == 0:
        return x
    elif x % 4 == 1:
        return x ^ (x - 1)
    elif x % 4 == 2:
        return x ^ (x - 1) ^ (x - 2)
    else:
        return 0


print(solve(a - 1) ^ solve(b))

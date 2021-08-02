a, b = list(map(int, input().split()))
c = min(a, b)


def fact(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res


print(fact(c))

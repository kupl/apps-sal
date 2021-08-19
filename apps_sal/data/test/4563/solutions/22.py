def cin():
    return list(map(int, input().split()))


def cino(test=False):
    if not test:
        return int(input())
    else:
        return input()


def cina():
    return list(map(int, input().split()))


a = cino()
(x, y) = (1, 1)
for _ in range(a):
    (p, q) = cin()
    k = max((x + p - 1) // p, (y + q - 1) // q)
    (x, y) = (k * p, k * q)
print(x + y)

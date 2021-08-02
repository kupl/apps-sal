K = int(input())


def dsum(n):
    return sum(list(map(int, str(n))))


def g(n):
    return n / dsum(n)


j = 1
order = 1
for i in range(K):
    print(j)
    if g(j + 10 ** (order - 1)) > g(j + 10 ** order):
        order += 1
    j += 10 ** (order - 1)

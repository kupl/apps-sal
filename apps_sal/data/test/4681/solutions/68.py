N = int(input())


def luca(n):
    a = 1
    b = 2
    for i in range(n):
        (a, b) = (a + b, a)
    return b


print(luca(N))

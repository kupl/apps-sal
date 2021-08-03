a, b = list(map(int, input().split(' ')))


def perform(a, b):
    steps = 0
    while a != 0 and b != 0:
        if a >= b:
            steps += a // b
        else:
            a, b = b, a
            steps += a // b
        a, b = b, a % b
    return steps


print(perform(a, b))

3


def gen(n, start, t):
    if n == 1:
        return [start]
    if t <= 2 ** (n - 2):
        return [start] + gen(n - 1, start + 1, t)
    else:
        return gen(n - 1, start + 1, t - 2 ** (n - 2)) + [start]


(n, t) = list(map(int, input().split()))
print(' '.join(map(str, gen(n, 1, t))))

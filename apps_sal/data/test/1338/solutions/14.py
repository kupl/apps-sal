
n, m = map(int, input().split())

def gen(n, m, now):
    if n == 1:
        return [now]
    if m <= 2 ** (n - 2):
        return [now] + gen(n - 1, m, now + 1)
    else:
        return gen(n - 1, m - 2 ** (n - 2), now + 1) + [now]

p = 2 ** (n - 2)

print(' '.join(map(str, gen(n, m, 1))))

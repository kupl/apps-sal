from itertools import product


def max2(x, y):
    return x if x > y else y


def min2(x, y):
    return x if x < y else y


(D, G) = list(map(int, input().split()))
pc = [tuple(map(int, input().split())) for _ in range(D)]
pc = [(p, c, 100 * i) for (i, (p, c)) in enumerate(pc, start=1)]
res = sum((p for (p, c, k) in pc))
for choice in product((True, False), repeat=D):
    t = sum((c + p * k for ((p, c, k), f) in zip(pc, choice) if f))
    steps = sum((p for ((p, c, k), f) in zip(pc, choice) if f))
    if t >= G:
        res = min2(res, steps)
        continue
    for ((p, c, k), f) in zip(reversed(pc), reversed(choice)):
        if not f:
            break
    if p * k + t >= G:
        steps += (G - t - 1) // k + 1
        res = min2(res, steps)
print(res)

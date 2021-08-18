
from collections import Counter

[n, a, b] = list(map(int, input().strip().split()))
bis = [tuple(map(int, input().strip().split())) for _ in range(n)]
dis = [(a * Vx - Vy, Vx) for x, Vx, Vy in bis]

dis.sort()


def count(d):
    return sum((v * k * (k - 1) for k, v in d))


def filt(it):
    return list(Counter(list(Counter(it).values())).items())


c_plus = count(filt((x for x, y in dis)))
c_minus = count(filt(dis))

print(c_plus - c_minus)

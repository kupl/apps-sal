import sys
import numpy as np

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

N, K = lr()
A = np.array(lr())
sum = A.sum()
# Aiが1以上のため、answerはsumの約数


def make_divisors(n):  # nの約数を列挙
    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    divisors.sort()
    return divisors


B = make_divisors(sum)

for x in B[::-1]:
    c = A % x
    c.sort()
    d = x - c
    c_cum = c.cumsum()
    d_cum = d.cumsum()

    for i in range(N):
        y = c_cum[i]
        z = d_cum[N - 1] - d_cum[i]
        if y > K or z > K:
            continue
        result = (y + z) // 2
        if result <= K:
            print(x)
            return

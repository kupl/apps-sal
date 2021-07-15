from itertools import accumulate
def BC132_F():
    n, k = list(map(int, input().split(' ')))
    mod = 10**9 + 7
    sqt = int(n**0.5)
    cnt = [n // i - n // (i + 1) for i in range(1, n // sqt)] + [1] * sqt
    x = cnt
    for _ in range(k):
        x = [(i * j) % mod for i, j in zip(accumulate(reversed(x)), cnt)]
    return x[-1]


print(BC132_F())

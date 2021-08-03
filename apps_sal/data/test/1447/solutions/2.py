from math import *

# logger[n] = log(n!)
logger = []
for n in range(1000111):
    if n == 0:
        logger.append(log(factorial(0)))
    else:
        logger.append(logger[n - 1] + log(n))


def binomial(n, k):
    if k < 0:
        return 0
    tmp = logger[n] - logger[k] - logger[n - k]
    return tmp


def main():
    n, m = [int(x) for x in input().split()]
    ans = 0
    for i in range(n):
        tmp = binomial((n - 1) * m, n - 1 - i) + binomial(m - 1, i) + log(i + 1)
        tmp -= (log(n) + binomial(n * m - 1, n - 1))
        ans += exp(tmp)
    print('%.12lf' % ans)


main()

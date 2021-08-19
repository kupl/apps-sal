import sys
from collections import defaultdict
mod = 10 ** 9 + 7


def factorization(n):
    """ n の素因数分解

    Args:
        n (int): [description]

    Returns:
        [type]: [description]
    """
    arr = []
    tmp = n
    for i in range(2, int(-(-n ** 0.5 // 1)) + 1):
        if tmp % i == 0:
            cnt = 0
            while tmp % i == 0:
                cnt += 1
                tmp //= i
            arr.append([i, cnt])
    if tmp != 1:
        arr.append([tmp, 1])
    if arr == []:
        arr.append([n, 1])
    return arr


def main():
    N = int(sys.stdin.readline().rstrip())
    A = [int(x) for x in sys.stdin.readline().rstrip().split()]
    p = defaultdict(int)
    for a in A:
        for (x, y) in factorization(a):
            p[x] = max(p[x], y)
    U = 1
    for (x, y) in p.items():
        U = U * pow(x, y, mod) % mod
    ans = 0
    for a in A:
        ans = (ans + U * pow(a, mod - 2, mod)) % mod
    print(ans)


main()

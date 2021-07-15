import sys
from collections import defaultdict

read = sys.stdin.read
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7


def prime_factorize(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n ** 0.5 // 1)) + 1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])
    if temp != 1:
        arr.append([temp, 1])
    if arr == []:
        arr.append([n, 1])
    return arr


def main():
    N = int(readline())
    d = defaultdict(int)
    for i in range(2, N + 1):
        P = prime_factorize(i)
        for x, n in P:
            d[x] = max(d[x], n)

    ans = 1
    for x, n in list(d.items()):
        ans *= x ** n
    ans += 1
    print(ans)


def __starting_point():
    main()

__starting_point()

MOD = 10 ** 9 + 7


def I():
    return list(map(int, input().split()))


(t,) = I()
while t:
    t -= 1
    (n, k) = I()
    print(n, 2 * n)

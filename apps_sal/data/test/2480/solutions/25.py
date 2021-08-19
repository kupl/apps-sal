import sys


def main():
    input = sys.stdin.readline
    (n, k) = map(int, input().split())
    a = list(map(int, input().split()))
    accum = [0] * n
    accum[0] = a[0]
    d = dict()
    ans = 0
    for i in range(1, n):
        accum[i] += a[i] + accum[i - 1]
    accum = [0] + accum
    for j in range(n + 1):
        if j - k >= 0:
            d[(accum[j - k] - (j - k)) % k] -= 1
        if (accum[j] - j) % k not in d:
            d[(accum[j] - j) % k] = 1
        else:
            ans += d[(accum[j] - j) % k]
            d[(accum[j] - j) % k] += 1
    return print(ans)


def __starting_point():
    main()


__starting_point()

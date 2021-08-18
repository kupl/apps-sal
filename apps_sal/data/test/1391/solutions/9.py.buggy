import sys

cases = False

# Pre-defined function
# Begin


def fast_pow(a: int, b: int):
    res = 1
    while b > 0:
        if b & 1:
            res *= a
        a *= a
        b >>= 1
    return res


def c2(n):
    return n * (n - 1) // 2


def get():
    return list(map(int, input().split()))


def bits(n: int):
    return list(bin(n)).count('1')


def main(test_case=False):
    n = int(input()) if test_case else 1
    for _ in range(n):
        test()


def flush():
    sys.stdout.flush()


def parr(arr):
    print(*arr, sep=' ')


def gcd(a, b):
    while b:
        if b % a == 0:
            break
        tmp = a
        a = b % a
        b = tmp
    return a


def ext_gcd(a: int, b: int):
    if (b == 0):
        return [a, [1, 0]]

    res = ext_gcd(b, a % b)
    g = res[0]
    x1 = res[1][0]
    y1 = res[1][1]
    x = y1
    y = x1 - y1 * (a // b)

    return [g, [x, y]]

# End


b = []
p = []
n = m = a = 0


def check(cnt):
    if cnt == 0:
        return True
    x = b[-cnt:]
    y = p[:cnt]
    s = a
    i = 0
    while i < cnt and s >= 0:
        s -= max(0, y[i] - x[i])
        i += 1
    return s >= 0


def test():
    nonlocal n, m, a, b, p
    n, m, a = get()
    b = sorted(get())
    p = sorted(get())

    left = 0
    right = min(n, m)

    ans = -1

    while left <= right:
        mid = (left + right) // 2
        if check(mid):
            ans = max(ans, mid)
            left = mid + 1
        else:
            right = mid - 1

    if ans == -1:
        print(0, 0)
        return

    # print(ans)

    t = 0
    x = b[-ans:]
    y = p[:ans]
    i = 0
    while i < ans:
        t += min(x[i], y[i])
        a -= max(0, y[i] - x[i])
        i += 1
    print(ans, max(0, t - a))


main(cases)

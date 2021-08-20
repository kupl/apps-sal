N = int(input())


def po(n, k):
    if k <= 0:
        return 0 <= n <= 1
    if k % 2 == 0 and -2 * (2 ** k - 1) // 3 <= n <= (2 ** (k + 2) - 1) // 3:
        return True
    elif k % 2 == 1 and -2 * (2 ** (k + 1) - 1) // 3 <= n <= (2 ** (k + 1) - 1) // 3:
        return True
    return False


def f(n):
    k = 0
    while True:
        if po(n, k):
            break
        k += 1
    ls = []
    while k >= 0:
        if po(n - (-2) ** k, k - 1):
            n -= (-2) ** k
            ls.append('1')
        else:
            ls.append('0')
        k -= 1
    return ''.join(ls)


print(f(N))

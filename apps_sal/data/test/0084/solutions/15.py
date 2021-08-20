def check9(x):
    i = len(x) - 1
    while i >= 0:
        if x[i] != '9':
            return len(x) - i - 1
        i -= 1
    return len(x) - i - 1


def solve(n):
    if n < 5:
        return n * (n - 1) // 2
    res = 0
    x = str(n + n - 1)
    length = len(x)
    if check9(x) == length:
        return 1
    cur = '9' * (length - 1)
    for i in range(9):
        c = str(i)
        p = int(c + cur)
        if p <= n + 1:
            res += p // 2
        elif p > n + n - 1:
            res += 0
        else:
            res += 1 + (n + n - 1 - p) // 2
    return res


n = int(input())
print(solve(n))

def task1(string):
    n = int(string[:string.index(' ')])
    k = int(string[string.index(' '):])
    if n % 2 == 0:
        if k <= n / 2:
            return 2 * k - 1
        else:
            return 2 * (k - n // 2)
    else:
        if k <= n // 2 + 1:
            return 2 * k - 1
        else:
            return 2 * (k - n // 2 - 1)


print(task1(input()))

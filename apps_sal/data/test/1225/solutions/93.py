def check(n):
    if n > 1:
        return 2 * (check(n // 2)) + 1
    else:
        return 1


print(check(int(input())))

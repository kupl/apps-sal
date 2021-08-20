(n, x) = map(int, input().split())
f_dict = {0: 1}


def f(n):
    if f_dict.get(n):
        return f_dict.get(n)
    return 3 + f(n - 1) * 2


patty_dict = {0: 1}


def total_patty(n):
    if patty_dict.get(n):
        return patty_dict.get(n)
    return 1 + 2 * total_patty(n - 1)


def count_patty(n, x):
    if n == 0 and x == 1:
        return 1
    elif x == 0:
        return 0
    elif 1 <= x and x <= f(n - 1) + 1:
        return count_patty(n - 1, x - 1)
    elif x == f(n - 1) + 2:
        return total_patty(n - 1) + 1
    elif f(n - 1) + 2 <= x and x <= 2 * f(n - 1) + 2:
        return total_patty(n - 1) + 1 + count_patty(n - 1, x - f(n - 1) - 2)
    else:
        return total_patty(n)


print(count_patty(n, x))

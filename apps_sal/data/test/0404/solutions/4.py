from math import sqrt as S


def num_div(n):
    if n == 1:
        return 1
    c = 2
    for i in range(2, int(S(n)) + 1):
        if n % i == 0:
            if i == n // i:
                c += 1
            else:
                c += 2
    return c


print(num_div(int(input())))

import numpy as np


def __starting_point():
    input_str = input()
    n = int(input_str)
    peterns = 10 ** n
    a0_subset = peterns - 9 ** n
    a9_subset = peterns - 9 ** n
    anti_subset = 8 ** n
    ans = a0_subset + a9_subset + anti_subset - peterns
    ans %= 10 ** 9 + 7
    print(ans)


__starting_point()

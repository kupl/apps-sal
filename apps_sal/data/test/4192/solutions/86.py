import numpy as np


def __starting_point():

    x = input()
    D, T, S = list(map(int, x.split(' ')))
    estimated_time = D / S
    if T >= estimated_time:
        print('Yes')
    else:
        print('No')


__starting_point()

import numpy as np


def __starting_point():

    n, x, m = list(map(int, input().split()))
    a = [0 for i in range(m + 2)]

    mod = [0 for i in range(m)]
    loop_start_0 = 0
    loop_start_1 = 0
    loop_exists = 0
    a[0] = x
    for i in range(1, m + 2):
        a[i] = a[i - 1]**2 % m
        if mod[a[i]] == 0:
            mod[a[i]] = i
        else:
            loop_start_0 = mod[a[i]]
            loop_start_1 = i
            loop_exists = 1
            break

    sum_of_a = 0

    if loop_exists:
        for i in range(loop_start_0):
            sum_of_a += a[i]

        loop_sum_of_a = 0
        for i in range(loop_start_0, loop_start_1):
            loop_sum_of_a += a[i]

        loop_num = np.floor((n - loop_start_0) / (loop_start_1 - loop_start_0))
        sum_of_a += loop_sum_of_a * loop_num

        for i in range(loop_start_0, int(n - (loop_start_1 - loop_start_0) * loop_num)):
            sum_of_a += a[i]

    else:
        for i in range(n):
            sum_of_a += a[i]

    print(int(sum_of_a))


__starting_point()

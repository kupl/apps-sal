import numpy as np

memory = {}


def recursive(n):
    if n < 3:
        return 0
    if n <= 5:
        return 1
    catch = memory.get(n)
    if catch is not None:
        return catch
    peterns = 1
    for i in range(3, n - 3 + 1):
        peterns += recursive(n - i)
    memory[n] = peterns
    return peterns


def __starting_point():

    input_str = input()
    s = int(input_str)
    ans = recursive(s)
    print((ans % (10**9 + 7)))


__starting_point()

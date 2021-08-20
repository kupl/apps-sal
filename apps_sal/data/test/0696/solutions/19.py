"""
Modular arithmetic:
This has something to do with Extended Euclidean Algorithm
"""


def cows_and_primitive_roots(p_int):
    if p_int == 2:
        return 1
    count = 0
    for x in range(2, p_int):
        x_to_i_mod_p = x
        divisible = False
        for i in range(2, p_int - 1):
            x_to_i_mod_p = x * x_to_i_mod_p % p_int
            if x_to_i_mod_p == 1:
                divisible = True
                break
        if not divisible:
            count += 1
    return count


def __starting_point():
    """
    Inside of this is the test. 
    Outside is the API
    """
    p = int(input())
    print(cows_and_primitive_roots(p))


__starting_point()

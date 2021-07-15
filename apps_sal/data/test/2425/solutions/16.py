import math

def find_largest_non_trivial_divisor(n):
    bound = min(math.ceil(math.sqrt(n) + 2) + 1, n)
    for d in range(2, bound):
        if n % d == 0:
            return d
    return n

num_tests = int(input())
for _ in range(num_tests):
    n = int(input())



    larg_bit_pos = 0
    x = n
    while x > 1:
        x //= 2
        larg_bit_pos += 1

    best0 = 2**(larg_bit_pos+1) - 1
    if n != best0:
        print(best0)
    else:
        d = find_largest_non_trivial_divisor(n)
        print(n // d)



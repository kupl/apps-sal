from math import sqrt, pow, log, log2, log10, exp
from copy import deepcopy
from fractions import gcd


def read_ints():
    return list(map(int, input().split()))


def read_int():
    return read_ints()[0]


def read_floats():
    return list(map(float, input().split()))


def read_float():
    return read_floats()[0]


def format_list(l):
    return ' '.join(list(map(str, l)))


def one_dim_array(n, value=0):
    return [deepcopy(value) for x in range(n)]


def two_dim_array(n, m, value=0):
    return [[deepcopy(value) for x in range(m)] for x in range(n)]


def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, sqrt(n) + 1):
        if n % i == 0:
            return False
    return True


def max_len_sublist(l, f):
    (start, max_length, length) = (0, 0, 0)
    for i in range(1, len(l)):
        if f(l[i], l[i - 1]):
            length += 1
        else:
            if max_length < length:
                start = i - length
                max_length = length
            length = 0
    return (start, max_length)


def tf_to_yn(b):
    return 'YES' if b else 'NO'


def longest_non_descent_subsequence(s, restore_sequence=False):
    d = one_dim_array(len(s), 0)
    for i in range(len(s)):
        possible = [d[j] + 1 if s[j] <= s[i] else 1 for j in range(i)]
        d[i] = 1 if len(possible) == 0 else max(possible)
    if not restore_sequence:
        return d[-1] if len(d) != 0 else 0


l = read_int()
p = read_int()
q = read_int()
t = l / (p + q)
print(t * p)

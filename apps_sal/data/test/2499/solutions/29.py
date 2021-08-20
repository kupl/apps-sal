import numpy as np
import sys
input = sys.stdin.readline


def print_ans(N, input_line):
    """Test Case
    >>> print_ans(3, "3 6 5")
    12
    >>> print_ans(4, "23 36 66 65")
    188
    >>> print_ans(20, "1008288677408720767 539403903321871999 1044301017184589821 215886900497862655 504277496111605629 972104334925272829 792625803473366909 972333547668684797 467386965442856573 755861732751878143 1151846447448561405 467257771752201853 683930041385277311 432010719984459389 319104378117934975 611451291444233983 647509226592964607 251832107792119421 827811265410084479 864032478037725181")
    2012721721873704572
    """
    ar = np.array(input_line.split(), 'int64')
    X = np.bitwise_xor.reduce(ar)
    ar = np.hstack((ar, np.array([1 << i for i in range(60) if X & 1 << i], 'int64')))
    for k in range(60)[::-1]:
        b = 1 << k
        j = ar & b != 0
        i = np.where(j & (ar < 2 * b))[0]
        if len(i):
            i = i[0]
            x = ar[i]
            ar[j] ^= x
            ar[i] = x
    r = np.bitwise_xor.reduce(ar)
    print(r + (r ^ X))


def __starting_point():
    N = int(input().rstrip())
    input_line = input().rstrip()
    print_ans(N, input_line)


__starting_point()

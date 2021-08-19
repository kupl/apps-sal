import numpy as np


def solve(*args: str) -> str:
    n = int(args[0])
    A = np.array(args[1].split(), dtype=np.int64)
    n_bit = len(np.binary_repr(max(A)))
    xor = np.bitwise_xor.reduce(A)
    A &= ~xor
    for b in reversed(list(range(n_bit))):
        b_set = A & 1 << b != 0
        msb_args = np.where(b_set & (A < 1 << b + 1))[0]
        if len(msb_args):
            b_set[msb_args[0]] = False
            A[b_set] ^= A[msb_args[0]]
    ret = 2 * np.bitwise_xor.reduce(A) + xor
    return str(ret)


def __starting_point():
    print(solve(*open(0).read().splitlines()))


__starting_point()

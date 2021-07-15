from numpy import int64, bitwise_xor

N, *A = map(int, open(0).read().split())
A = int64(A)

x = bitwise_xor.reduce(A)
A &= ~x

res = 0
while any(A):
    ma = A.max()
    msb = 1 << (int(ma).bit_length() - 1)

    A[(A & msb) > 0] ^= ma

    res ^= ma * (not res & msb)

print(x + 2 * res)

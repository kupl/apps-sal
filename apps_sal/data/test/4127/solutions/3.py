
def ri():
    return int(input())


def rii():
    return [str(v) for v in input().split()]


A, B = rii()
A = int(A)
B, F = [int(v) for v in B.split(".")]
B = 100 * B + F

print((A * B) // 100)

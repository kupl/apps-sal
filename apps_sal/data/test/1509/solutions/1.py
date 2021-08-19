N = int(input())
A = [int(a) for a in input().split()]


def calc(a0, b0):
    (a, b) = (min(a0, b0), max(a0, b0))
    return b - 1 + (a - 1) * (b - a - 1) + N - a + (b - a - 1) * (N - b)


def calc0(a):
    return N + (a - 1) * (N - a)


s = calc0(A[0]) + calc0(A[-1])
for i in range(N - 1):
    s += calc(A[i], A[i + 1])
print(s // 2)

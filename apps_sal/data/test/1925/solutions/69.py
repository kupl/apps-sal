from math import floor

A, B, N = map(int, input().split())
def f(x): return floor(A * x / B) - A * floor(x / B)


if A == 1 or B == 1:
    print(0)
    return
if N < B:
    print(f(N))
    return
print(f(B - 1))

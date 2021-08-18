import math


def LCM(a, b):
    g = math.gcd(a, b)
    return a * b // g


N, M = list(map(int, input().split()))
A = list(map(int, input().split()))
A = list(set(A))
N = len(A)
a0 = A[0]
div = 1
while a0 % 2 == 0:
    div *= 2
    a0 //= 2

for i in range(1, N):
    a = A[i] % div
    b = A[i] // div
    if (b % 2 == 0) or (a != 0):
        print((0))
        return

for i in range(N):
    A[i] //= 2

if N > 1:
    lcm = LCM(A[0], A[1])
    for i in range(2, N):
        lcm = LCM(lcm, A[i])

if N == 1:
    lcm = A[0]

ans = M // lcm
if ans % 2 == 1:
    print((ans // 2 + 1))
else:
    print((ans // 2))

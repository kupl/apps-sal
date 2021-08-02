import math

N, M = list(map(int, input().split()))
if abs(N - M) >= 2:
    print((0))
    return


N = math.factorial(N) % (10 ** 9 + 7)
M = math.factorial(M) % (10 ** 9 + 7)
if N == M:
    print(((N * M * 2) % (10 ** 9 + 7)))
else:
    print(((N * M) % (10 ** 9 + 7)))

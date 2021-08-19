import math
(N, M) = (int(T) for T in input().split())
if M - 2 * N > 0:
    Convert = int(math.floor((M - 2 * N) / 4))
    N += Convert
    M -= 2 * Convert
    print(N)
else:
    print(M // 2)

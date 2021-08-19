import math as m
(N, M) = map(int, input().split())
w = 1000000007
if abs(N - M) < 2:
    if N == M:
        print(m.factorial(N) ** 2 * 2 % w)
    else:
        print(m.factorial(N) * m.factorial(M) % w)
else:
    print(0)

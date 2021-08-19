from math import factorial as fac
(N, M) = map(int, input().split())
if abs(N - M) > 1:
    print(0)
elif abs(N - M) == 1:
    print(fac(N) * fac(M) % 1000000007)
else:
    print(2 * fac(N) * fac(M) % 1000000007)

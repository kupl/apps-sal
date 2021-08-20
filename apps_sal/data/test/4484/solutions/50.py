from math import factorial
(N, M) = list(map(int, input().split()))
mod = 10 ** 9 + 7
if abs(N - M) > 1:
    print(0)
elif abs(N - M) == 1:
    print(factorial(N) * factorial(M) % mod)
else:
    print(2 * factorial(N) * factorial(M) % mod)

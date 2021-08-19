mod = 10 ** 9 + 7


def factorial(n, mod):
    fact = 1
    for integer in range(1, n + 1):
        fact *= integer
        fact %= mod
    return fact


(N, M) = map(int, input().split())
if abs(N - M) > 1:
    print(0)
else:
    ans = 1
    ans *= factorial(N, mod)
    ans *= factorial(M, mod)
    ans *= 2 - abs(N - M)
    ans %= mod
    print(ans)

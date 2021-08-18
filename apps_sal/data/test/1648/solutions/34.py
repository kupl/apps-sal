from math import factorial
N, K = list(map(int, input().split()))


for k in range(1, K + 1):
    if k > N - K + 1:
        print((0))
        continue

    c1 = factorial(K - 1) // (factorial(K - k) * factorial(k - 1))
    c1 = int(c1) % (10 ** 9 + 7)

    c2 = factorial(N - K + 1) // (factorial(N - K - k + 1) * factorial(k))
    c2 = int(c2) % (10**9 + 7)

    ans = c1 * c2 % (10**9 + 7)
    print(ans)

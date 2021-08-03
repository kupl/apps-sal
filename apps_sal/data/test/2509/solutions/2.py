N, K = 5, 2

# N, K = 31415, 9265
#
# N, K = 10, 0

N, K = list(map(int, input().split()))


def calculate(n, k):
    result = 0
    for b in range(1, N + 1):
        p = n // b
        s1 = p * max(0, (b - 1 - (k - 1)))
        s2 = max(0, (n % b) - (k - 1))

        res = s1 + s2
        if k == 0:
            result = result + res - 1
        else:
            result = result + res

    print(result)


calculate(N, K)

def ceil(a, b):
    return a // b + bool(a % b)


def solve(n, m, k):
    c = n // k
    j1 = min(c, m)
    m -= j1
    return j1 - ceil(m, k - 1)


for _ in range(int(input())):
    (n, m, k) = list(map(int, input().split()))
    print(solve(n, m, k))

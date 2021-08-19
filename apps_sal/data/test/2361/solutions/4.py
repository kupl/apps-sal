t = int(input())

for _ in range(t):
    n, m, k = [int(x) for x in input().split()]
    np1 = min(m, n // k)
    m -= np1
    # the remainder divided over k - 1 players (rounded up)
    np2 = (m + k - 2) // (k - 1)
    print(np1 - np2)

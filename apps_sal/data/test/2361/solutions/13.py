for _ in range(int(input())):
    (n, m, k) = list(map(int, input().split()))
    cardsPerPlayer = n // k
    x = min(cardsPerPlayer, m)
    m -= x
    print(x - (m + k - 2) // (k - 1))

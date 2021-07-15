for _ in range(int(input())):
    n, m, k = map(int, input().split())
    cards = n // k
    x = min(m, cards)
    y = __import__('math').ceil((m - x) / (k-1))
    print(x - y)

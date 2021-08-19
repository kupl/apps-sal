(n, z, w) = map(int, input().split())
cards = list(map(int, input().split()))
if abs(cards[len(cards) - 1] - w) > abs(cards[len(cards) - 1] - cards[len(cards) - 2]):
    print(abs(cards[len(cards) - 1] - w))
else:
    print(abs(cards[len(cards) - 1] - cards[len(cards) - 2]))

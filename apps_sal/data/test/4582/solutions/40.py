deck = ["H", "D"]
a, b = input().split()
if deck.index(a) == 0:
    print(b)
elif deck.index(b) == 0:
    print(deck[1])
else:
    print(deck[0])

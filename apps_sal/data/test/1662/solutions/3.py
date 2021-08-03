n = input()
cards = input().split(" ")
cards = [int(cards[i]) for i in range(len(cards))]

if len(cards) == len(list(set(cards))):
    print(n)
    cards.sort()
    for i in range(len(cards) - 1, 0, -1):
        print(cards[i], end=" ")
    print(cards[0], end="\n")
else:
    cards.sort()
    mycards = [cards[0]]

    cards[0] = None
    for i in range(1, len(cards)):
        if cards[i] > mycards[-1]:
            mycards.append(cards[i])
            cards[i] = None

    for i in range(len(cards) - 1, -1, -1):
        if cards[i] == None:
            continue

        if cards[i] < mycards[-1]:
            mycards.append(cards[i])
            cards[i] = None

    print(len(mycards))
    for i in range(len(mycards) - 1):
        print(mycards[i], end=" ")
    print(mycards[-1], end="\n")

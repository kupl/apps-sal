cardNum = int(input())

cards = [input() for i in range(cardNum)]

values = {}
if len(set(cards)) > 2:
    print("NO")
else:
    for card in set(cards):
        value = cards.count(card)
        if value in values:
            print("YES")
            print(card, values[value])
            break
        values[value] = card
    else:
        print("NO")

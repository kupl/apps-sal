__author__ = 'maaanu'


def start():
    m = int(input())
    cards = [int(x) for x in input().split(" ")]
    cards.sort()
    max_cards = len(cards)
    last_card = cards.pop()
    table = [last_card]

    for val in reversed(cards):
        if val < last_card:
            last_card = val
            table.append(last_card)
        elif val < table[0]:
            table.insert(0, val)
        else:
            max_cards -= 1
    print(max_cards)
    print("".join([str(number) + " " for number in table]))


start()

N = int(input())

cards = [int(s) for s in input().split()]
list.sort(cards, reverse=True)
a_cards = cards[0::2]
b_cards = cards[1::2]
print(sum(a_cards) - sum(b_cards))

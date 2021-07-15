n = int(input())
all_cards = list(map(int, input().split()))
all_cards.sort(reverse=True)

alice_cards = []
bob_cards = []

for i in range(n):
    if i % 2 == 0:
        alice_cards.append(all_cards[i])
    if i % 2 == 1:
        bob_cards.append(all_cards[i])

print(sum(alice_cards)-sum(bob_cards))

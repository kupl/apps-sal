N = int(input())
cards = list(map(int, input().split()))
alice = []
bob = []

cards.sort(reverse=True)

for i in range(N):
    if i % 2 == 0:
        alice.append(cards[i])
    else:
        bob.append(cards[i])

print((sum(alice) - sum(bob)))

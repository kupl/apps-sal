N = int(input())
a = list(map(int, input().split()))

card = list(a)
card.sort(reverse=True)
Alice = []
Bob = []

if len(card) % 2 != 0:
    Alice.append(card[-1])
    card.pop(-1)

while card:
    Alice.append(card[0])
    Bob.append(card[1])
    card.pop(0)
    card.pop(0)

print((sum(Alice) - sum(Bob)))

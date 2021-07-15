n = int(input())
blue_cards = []
for i in range(n):
    blue_cards.append(input())

m = int(input())
red_cards = []
for i in range(m):
    red_cards.append(input())

scores = []
for i in range(len(blue_cards)):
    score = blue_cards.count(blue_cards[i]) - red_cards.count(blue_cards[i])
    scores.append(score)

if max(scores) < 0:
    print((0))
else:
    print((max(scores)))


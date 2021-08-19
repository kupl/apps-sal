n = int(input())
s1 = [int(card) for card in input().split()]
s2 = [int(card) for card in input().split()]
s1 = s1[1:]
s2 = s2[1:]
magic = 1000000
fights = 0
flag = False
while True:
    (card1, card2) = (s1.pop(0), s2.pop(0))
    fights += 1
    if fights > magic:
        flag = True
        break
    if card1 > card2:
        s1.append(card2)
        s1.append(card1)
    else:
        s2.append(card1)
        s2.append(card2)
    if s1 == []:
        winner = 2
        break
    if s2 == []:
        winner = 1
        break
if flag:
    print(-1)
else:
    print(fights, winner)

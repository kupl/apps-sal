num = int(input())
cards = input()
cards = [int(i) for i in cards.split()]
begin = 0
end = num - 1
sereja = 0
dima = 0
turn = 0
for i in range(0, num):
    if turn == 0:
        if cards[begin] > cards[end]:
            sereja += cards[begin]
            begin += 1
        else:
            sereja += cards[end]
            end -= 1
        turn = 1
    else:
        if cards[begin] > cards[end]:
            dima += cards[begin]
            begin += 1
        else:
            dima += cards[end]
            end -= 1
        turn = 0
print(sereja, dima)

kingMove = list(input())
possMoves = 3
if kingMove[0] > 'a' and kingMove[0] < 'h':
    possMoves += 2
if int(kingMove[1]) > 1 and int(kingMove[1]) < 8:
    possMoves += 2
if possMoves == 7:
    possMoves += 1
print(possMoves)

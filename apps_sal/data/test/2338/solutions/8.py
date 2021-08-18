from sys import stdin, stdout

n = int(stdin.readline())
pos = []
for i in range(n):
    x, y = list(map(int, stdin.readline().split()))
    pos.append([x, y])
pos = sorted(pos, key=lambda pos: abs(pos[0]) + abs(pos[1]))
moves = []
for p in pos:
    x, y = p
    xNeg, yNeg = False, False
    xPos, yPos = False, False
    if x > 0:
        moves.append("1 {} R".format(x))
        xPos = True
    elif x < 0:
        moves.append("1 {} L".format(-x))
        xNeg = True

    if y > 0:
        moves.append("1 {} U".format(y))
        yPos = True
    elif y < 0:
        moves.append("1 {} D".format(-y))
        yNeg = True
    moves.append("{}".format(2))
    if xNeg:
        moves.append("1 {} R".format(-x))
    elif xPos:
        moves.append("1 {} L".format(x))

    if yNeg:
        moves.append("1 {} U".format(-y))
    elif yPos:
        moves.append("1 {} D".format(y))
    moves.append("{}".format(3))

print(len(moves))
for m in moves:
    stdout.write(m)
    stdout.write("\n")

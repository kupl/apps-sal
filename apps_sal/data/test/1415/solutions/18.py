(n, m, x, y) = [int(x) for x in input().split(' ')]
commands = input()
(x, y) = (x - 1, y - 1)
move = dict([('U', (-1, 0)), ('D', (1, 0)), ('L', (0, -1)), ('R', (0, 1))])
place = set()
place.add((x, y))
print('1', end=' ')
for command in commands[:-1]:
    (oldX, oldY) = (x, y)
    (x, y) = (x + move[command][0], y + move[command][1])
    if (x < 0 or y < 0) or (x >= n or y >= m):
        print('0', end=' ')
        (x, y) = (oldX, oldY)
        continue
    elif (x, y) in place:
        print(0, end=' ')
    else:
        print('1', end=' ')
    place.add((x, y))
(x, y) = (x + move[commands[-1]][0], y + move[commands[-1]][1])
if (x < 0 or y < 0) or (x >= n or y >= m):
    print('0')
else:
    print(n * m - len(place))

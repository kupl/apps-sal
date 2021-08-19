inp = str(input()).split(' ')
(w, h) = (int(inp[0]), int(inp[1]))
image = []
for x in range(h):
    row = str(input())
    image.append([x for x in row])


def turn90():
    turned = []
    for x in range(w):
        row = []
        for y in range(h):
            row.append(image[y][x])
        turned.append(row)
    return turned


image = turn90()


def mirror():
    mirroed = []
    for row in image:
        row.reverse()
        mirroed.append(row)
    return mirroed


def multiply():
    multi = []
    for row in image:
        multi.append(''.join([y * 2 for y in row]))
        multi.append(''.join([y * 2 for y in row]))
    for row in multi:
        print(''.join(row))


multiply()

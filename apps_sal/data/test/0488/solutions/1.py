name = input()

blocks = []
now = name[0]
counter = 1
for x in range(1, len(name)):
    if name[x] != now:
        blocks.append((now, counter))
        now = name[x]
        counter = 1
    else:
        counter += 1
blocks.append((now, counter))

counter = 0
temp = []
while len(blocks) > 1:
    counter += 1
    temp = []
    (x, y) = blocks[0]
    if y > 1:
        temp.append((x, y - 1))
    for s in range(1, len(blocks) - 1):
        (x, y) = blocks[s]
        if len(temp) > 0:
            (tempx, tempy) = temp[-1]
            if y > 2:
                if x != tempx:
                    temp.append((x, y - 2))
                else:
                    temp[-1] = (x, tempy + y - 2)
        else:
            if y > 2:
                temp.append((x, y - 2))

    (x, y) = blocks[-1]
    if len(temp) > 0:
        (tempx, tempy) = temp[-1]
        if y > 1:
            if x != tempx:
                temp.append((x, y - 1))
            else:
                temp[-1] = (x, tempy + y - 1)
    else:
        if y > 1:
            temp.append((x, y - 1))
    blocks = temp

print(counter)

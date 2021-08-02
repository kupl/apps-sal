def take_lightest_box(boxes):

    for i in range(101):
        if i in boxes:
            boxes[i] -= 1
            if boxes[i] == 0:
                del boxes[i]
            return i


piles = []


boxes = {}

input()
tmp = input()

x = [int(i) for i in tmp.split(" ")]

for item in x:
    if item in boxes:
        boxes[item] = boxes[item] + 1
    else:
        boxes[item] = 1

while len(boxes) > 0:
    lightest = take_lightest_box(boxes)

    for pile in piles:
        if len(pile) <= lightest:
            pile.append(lightest)
            break
    else:
        piles.append([lightest])


print(len(piles))

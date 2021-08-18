
KEYS = {
    1: (0, 0),
    2: (1, 0),
    3: (2, 0),
    4: (0, 1),
    5: (1, 1),
    6: (2, 1),
    7: (0, 2),
    8: (1, 2),
    9: (2, 2),
    0: (1, 3)
}

BOARD = set(KEYS.values())

n = int(input())
number = list(map(int, list(input())))


def add_offset(cell, offset):
    return (cell[0] + offset[0], cell[1] + offset[1])


uniq = True

for posible_starts in BOARD:
    if KEYS[number[0]] != posible_starts:
        all_fit = True
        off = (posible_starts[0] - KEYS[number[0]][0],
               posible_starts[1] - KEYS[number[0]][1])
        for num_part in number:
            if add_offset(KEYS[num_part], off) not in BOARD:
                all_fit = False
                break
        if all_fit:
            uniq = False

if uniq:
    print("YES")
else:
    print("NO")

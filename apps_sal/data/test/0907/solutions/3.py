from itertools import permutations, combinations
from sys import stdin


def input():
    return stdin.readline().strip()


(m, n) = list(map(int, input().split()))
pairs = []
for i in range(n):
    (a, b) = list(map(int, input().split()))
    pairs.append((a, b))
if n == 1:
    print('YES')
else:
    possible = set([pairs[0][0], pairs[0][1]])
    flag = True
    for i in range(n):
        if pairs[i][0] in possible or pairs[i][1] in possible:
            continue
        elif len(possible) == 4:
            flag = False
            break
        else:
            possible.add(pairs[i][0])
            possible.add(pairs[i][1])
    if flag:
        possible = list(possible)
        x_y = list(combinations(possible, 2))
        for (x, y) in x_y:
            x_y_ = set([x, y])
            flag = True
            for i in range(n):
                if pairs[i][0] in x_y_ or pairs[i][1] in x_y_:
                    continue
                else:
                    flag = False
                    break
            if flag:
                break
    if flag:
        print('YES')
    else:
        print('NO')

from itertools import combinations
n = int(input())
colors = {'R': 0, 'G': 1, 'B': 2, 'Y': 3, 'W': 4}
letters = {'1': 0, '2': 1, '3': 2, '4': 3, '5': 4}
l = list(set(list(input().split())))


def checker(hint, cards):
    for i in cards:
        for j in cards:
            if i == j:
                continue
            if i[0] == j[0]:
                if i[1] not in hint and j[1] not in hint:
                    return False
            elif i[1] == j[1]:
                if i[0] not in hint and j[0] not in hint:
                    return False
            elif i[0] not in hint and i[1] not in hint and (j[0] not in hint) and (j[1] not in hint):
                return False
    return True


result = []
for i in l:
    if i[0] not in result:
        result.append(i[0])
    if i[1] not in result:
        result.append(i[1])
all_hints = []
for i in range(1, len(result) + 1):
    comb = combinations(result, i)
    all_hints += comb
min_hint = len(result)
if len(l) == 1:
    print(0)
else:
    for i in all_hints:
        if checker(i, l):
            min_hint = min(len(i), min_hint)
    print(min_hint)

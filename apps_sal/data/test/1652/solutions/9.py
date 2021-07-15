# author:  Taichicchi
# created: 03.11.2020 02:00:47

import sys

LS = [
    list("dream")[::-1],
    list("dreamer")[::-1],
    list("erase")[::-1],
    list("eraser")[::-1],
]

S = list(input())[::-1]

while S:
    if S[:7] == LS[1]:
        # print(f"{LS[1]}\t:\t{S[:7]}")
        for l in LS[1]:
            S.remove(l)
    elif S[:6] == LS[3]:
        # print(f"{LS[3]}\t:\t{S[:6]}")
        for l in LS[3]:
            S.remove(l)
    elif S[:5] == LS[0]:
        # print(f"{LS[0]}\t:\t{S[:5]}")
        for l in LS[0]:
            S.remove(l)
    elif S[:5] == LS[2]:
        # print(f"{LS[2]}\t:\t{S[:5]}")
        for l in LS[2]:
            S.remove(l)
    else:
        print("NO")
        return
print("YES")


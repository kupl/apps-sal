__author__ = 'Andrey'


def count_clean():
    nonlocal room
    nonlocal n
    c = 0
    for row in room:
        if sum(row) == n:
            c += 1
    return c


def invert(row):
    nonlocal room
    nonlocal n
    cleaned = []
    for i in range(n):
        if room[row][i] == 0:
            for j in range(n):
                room[j][i] = 1 - room[j][i]
            cleaned.append(i)
    c = count_clean()
    for w in cleaned:
        for j in range(n):
            room[j][w] = 1 - room[j][w]
    return c


room = []
m = 0
n = int(input())
for q in range(n):
    room.append(list(map(int, list(input()))))
for i in range(n):
    m = max(invert(i), m)
print(m)

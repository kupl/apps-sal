# -*- coding: utf-8 -*-

n = int(input())
cards = [[set(map(int, input().split()[1:])), i, True] for i in range(n)]

cards.sort(key=lambda x: len(x[0]))
for i in range(n-1, -1, -1):
    if not cards[i][2]:
        continue
    for j in range(0, i):
        if cards[j][0] == cards[i][0]:
            cards[j][2] = cards[i][2] = False
            break
        if cards[j][0] < cards[i][0]:
            cards[i][2] = False
            break

cards.sort(key=lambda x: x[1])
for card in cards:
    print('YES' if card[2] else 'NO')


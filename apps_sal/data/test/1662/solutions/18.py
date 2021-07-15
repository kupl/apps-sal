#!/usr/bin/env python3.3
# -*- coding: utf-8 -*-

def sereja_and_stairs ():

    m = input()
    b = input()

    nr_allcards = int(m)
    cards = list(map(int, b.split(' ')))

    nr_cards = [0] * 5001
    max_card = 0
    for card in cards:
        nr_cards[card] += 1
        max_card = max(max_card, card)

    up_stairs = []
    down_stairs = []
    for card in range(1, max_card+1):
        if nr_cards[card] > 0:
            nr_cards[card] -= 1
            down_stairs.append(card)
        if nr_cards[card - 1] > 0:
            up_stairs.append(card - 1)
    down_stairs.reverse()
    stairs = up_stairs + down_stairs

    nr_stairs = len(stairs)
    stairs = ' '.join(map(str,stairs))
    print(('{nr:d}\n{stairs:s}'
          .format(nr=nr_stairs, stairs=stairs)
          ))

    return

def __starting_point():
    sereja_and_stairs()

__starting_point()

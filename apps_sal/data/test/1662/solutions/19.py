#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Python 3
def sereja_and_stairs():

    ##
    # raw_input() → input()
    m = input()
    b = input()

    ##
    # nr_allcards = int(m)          #
    cards = list(map(int, b.split(' ')))  #

    ##
    nr_cards = [0] * 5001           #
    max_card = 0                    #
    for card in cards:
        nr_cards[card] += 1
        max_card = max(max_card, card)

    ##
    #
    #
    up_stairs = []                  #
    down_stairs = []                #
    for card in range(1, max_card + 1):
        #
        if nr_cards[card] > 0:
            nr_cards[card] -= 1
            down_stairs.append(card)
        #
        if nr_cards[card - 1] > 0:
            up_stairs.append(card - 1)

    ##
    down_stairs.reverse()
    stairs = up_stairs + down_stairs

    ##
    #
    #
    # [Python2] : print '%d\n%s' % (nr_stairs, stairs)
    # [Python3] : print('{number:d}\n{stairs:s}'.format(number=nr_stairs, stairs=stairs))
    nr_stairs = len(stairs)
    stairs = ' '.join(map(str, stairs))
    print('{number:d}\n{stairs:s}'.format(number=nr_stairs, stairs=stairs))
    return


def __starting_point():
    sereja_and_stairs()


__starting_point()

import sys
import collections


def get_code(first_cards, second_cards):
    c1 = 0
    for i, card in enumerate(first_cards):
        c1 += (card - 1) * 10**i
    c2 = 0
    for i, card in enumerate(second_cards):
        c2 += (card - 1) * 10**i
    return (c1, c2)


def main():
    n = int(sys.stdin.readline())
    first_cards = collections.deque(reversed(list(map(int, sys.stdin.readline().split()))[1:]))
    second_cards = collections.deque(reversed(list(map(int, sys.stdin.readline().split()))[1:]))


    existing_states = set()
    number_of_fights = 0

    while first_cards and second_cards:
        # code = get_code(first_cards, second_cards)
        code = (tuple(first_cards), tuple(second_cards))
        if code in existing_states:
            print (-1)
            return
        existing_states.add(code)

        if first_cards[-1] > second_cards[-1]:
            first_cards.appendleft(second_cards.pop())
            first_cards.appendleft(first_cards.pop())
        else:
            second_cards.appendleft(first_cards.pop())
            second_cards.appendleft(second_cards.pop())
        number_of_fights += 1

    print ('%d %d' % (number_of_fights, 1 if not second_cards else 2))


def __starting_point():
    main()
__starting_point()

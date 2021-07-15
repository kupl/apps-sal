from collections import deque

def main():

    players = {
        'a': None,
        'b': None,
        'c': None
    }

    for i in players:
        players[i] = deque(tuple(input()))

    card = 'a'
    while players[card]:
        card = players[card].popleft()

    print(card.upper())


def __starting_point():
    main()
__starting_point()

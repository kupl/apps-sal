def main():
    input()
    seq = input()

    LEFT = {
        '0': False,
        '1': False,
        '2': True,
        '3': True,
        '4': False,
        '5': True,
        '6': True,
        '7': False,
        '8': True,
        '9': True,
    }
    RIGHT = {
        '0': False,
        '1': True,
        '2': True,
        '3': False,
        '4': True,
        '5': True,
        '6': False,
        '7': True,
        '8': True,
        '9': False,
    }
    UP = {
        '0': True,
        '1': False,
        '2': False,
        '3': False,
        '4': True,
        '5': True,
        '6': True,
        '7': True,
        '8': True,
        '9': True,
    }
    DOWN = {
        '0': False,
        '1': True,
        '2': True,
        '3': True,
        '4': True,
        '5': True,
        '6': True,
        '7': False,
        '8': True,
        '9': False,
    }
    print('NO' if any(all(can[n] for n in seq) for can in (LEFT, RIGHT, UP, DOWN)) else 'YES')


def __starting_point():
    main()


__starting_point()

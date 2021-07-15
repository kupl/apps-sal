def next_animal(before, current, claim):
    if (before == current and claim == 'x') or \
        (before != current and claim == 'o'):
        return 'W'
    else:
        return 'S'


def search(S):
    assert len(S) > 2
    init_twos = ['SS', 'SW', 'WS', 'WW']
    ret = ''
    for init_two in init_twos:
        animals = init_two
        for i in range(1, len(S) - 1):
            a = next_animal(animals[i - 1], animals[i], S[i])
            animals += a
        # check: claim of first and last animals
        if animals[1] != next_animal(animals[-1], animals[0], S[0]):
            continue
        if animals[0] != next_animal(animals[-2], animals[-1], S[-1]):
            continue
        ret = animals
        break
    return ret


def main():
    N = int(input())
    S = input()
    ret = search(S)
    if len(ret) > 0:
        print(ret)
    else:
        print((-1))


def __starting_point():
    main()

__starting_point()

__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = 'sonhuytran@gmail.com'
__doc__ = ''
__version__ = '1.0'


def main() -> int:
    n_wires = int(input())
    birds_in_wires = [0] + [int(word) for word in input().split()]
    n_shots = int(input())
    for i in range(n_shots):
        (x, y) = map(int, input().split())
        birds = birds_in_wires[x]
        left_birds = y - 1
        right_birds = birds - y
        birds_in_wires[x] = 0
        if x > 1:
            birds_in_wires[x - 1] += left_birds
        if x < n_wires:
            birds_in_wires[x + 1] += right_birds
    print('\n'.join([str(birds_in_wires[i]) for i in range(1, n_wires + 1)]))
    return 0


def __starting_point():
    main()
    return


__starting_point()

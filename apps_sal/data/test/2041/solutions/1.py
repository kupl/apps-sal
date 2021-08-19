import sys
WIDTH = 10


def index_tree(n):
    levels = [[1] * n]

    size = WIDTH
    while size < n:
        m, r = n // size, n % size
        levels.append([size] * m + ([r] if r > 0 else []))
        size *= WIDTH

    return levels


def dec_index(levels, i):
    for level in levels:
        level[i] -= 1
        i //= WIDTH


def find_pos(levels, pos):
    i, l = 0, len(levels) - 1

    total = 0
    while True:
        level = levels[l]
        while total + level[i] < pos:
            total += level[i]
            i += 1

        if l == 0:
            return i
        i *= WIDTH
        l -= 1


def main():
    # INPUT
    numbers = [int(x) for x in sys.stdin.read().split()]
    n = numbers[0]
    sequence = numbers[1:n + 1]
    m = numbers[n + 1]

    queries = {}
    for i in range(n + 2, n + 2 + 2 * m, 2):
        k, pos = numbers[i], numbers[i + 1]
        if k in queries:
            queries[k][pos] = None
        else:
            queries[k] = {pos: None}

    # WORK
    sequence1 = sorted([(s, -i) for i, s in enumerate(sequence)])
    tree = index_tree(n)
    size = n

    for _, neg_i in sequence1:
        if size in queries:
            for pos in queries[size]:
                queries[size][pos] = find_pos(tree, pos)

        dec_index(tree, -neg_i)
        size -= 1

    # PRINT
    for i in range(n + 2, n + 2 + 2 * m, 2):
        k, pos = numbers[i], numbers[i + 1]
        print(sequence[queries[k][pos]])


main()

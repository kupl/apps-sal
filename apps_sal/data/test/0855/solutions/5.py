def get_ints():
    return [int(n) for n in input().split()]


def move(matrix, a, b):
    return matrix[a][b]


def game(a, b):
    res = (a - b) % 3
    if res == 1:
        return (1, 0)
    elif res == 2:
        return (0, 1)
    else:
        return (0, 0)


def __starting_point():
    z = get_ints()
    assert len(z) == 3
    (k, a, b) = (z[0], z[1] - 1, z[2] - 1)
    alice = list()
    for i in range(3):
        z = get_ints()
        assert len(z) == 3
        for j in range(len(z)):
            z[j] -= 1
        alice.append(z.copy())
    bob = list()
    for i in range(3):
        z = get_ints()
        assert len(z) == 3
        for j in range(len(z)):
            z[j] -= 1
        bob.append(z.copy())
    moves = list()
    results = list()
    index = -1
    for m in range(k):
        if (a, b) in moves:
            index = moves.index((a, b))
            break
        moves.append((a, b))
        results.append(game(a, b))
        (a, b) = (move(alice, a, b), move(bob, a, b))
    (apoint, bpoint) = (0, 0)
    c = len(moves) - index
    rep = (k - index) // c
    for res in results[index:]:
        (da, db) = res
        apoint += da
        bpoint += db
    apoint *= rep
    bpoint *= rep
    rem = (k - index) % c
    for i in range(rem):
        (da, db) = results[i + index]
        apoint += da
        bpoint += db
    for res in results[:index]:
        (da, db) = res
        apoint += da
        bpoint += db
    print(apoint, bpoint)


__starting_point()

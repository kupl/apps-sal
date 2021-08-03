

def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def solve():
    """
    4 2 1 3 5

    0 2 3 4 1 1 0 2 2
    x x x x x x x x x

    1 5 8 3 4 2 7 6 9

10
0 3 4 2

0 1 2 3 4 5
    """
    N = read_int()
    shakes = [[] for _ in range(N)]

    for i, a in enumerate(read_ints(), start=1):
        shakes[a].append(i)
    i = 0
    answer = []
    while N > 0:
        if len(shakes[i]) > 0:
            answer.append(shakes[i].pop())
            N -= 1
            i += 1
        else:
            j = i
            while j >= 0 and len(shakes[j]) == 0:
                j -= 3
            if j < 0:
                break
            i = j
    if N != 0:
        return 'Impossible'
    print('Possible')
    return ' '.join(map(str, answer))


def __starting_point():
    print(solve())


__starting_point()

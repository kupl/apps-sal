from collections import deque


def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def solve():
    N, K, C = read_ints()
    S = input().strip()
    earliest = []
    i = 0
    while len(earliest) < K:
        if S[i] == 'o':
            earliest.append(i)
            i += C + 1
        else:
            i += 1
    latest = []
    i = N - 1
    while len(latest) < K:
        if S[i] == 'o':
            latest.append(i)
            i -= C + 1
        else:
            i -= 1
    latest.reverse()
    for i, j in zip(earliest, latest):
        if i == j:
            print((i + 1))


def __starting_point():
    solve()


__starting_point()

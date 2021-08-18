
from collections import Counter


def resolve():
    N = int(input())
    A = list(map(int, input().split()))

    O = Counter(A[::2])
    E = Counter(A[1::2])

    most_O = O.most_common(2)
    most_E = E.most_common(2)
    most_O.append((0, 0))
    most_E.append((0, 0))

    cnt = 0
    if most_O[0][0] == most_E[0][0]:
        res1 = most_O[0][1] + most_E[1][1]
        res2 = most_O[1][1] + most_E[0][1]
        cnt = max(res1, res2)
    else:
        cnt = most_O[0][1] + most_E[0][1]

    print((N - cnt))


def __starting_point():
    resolve()


__starting_point()

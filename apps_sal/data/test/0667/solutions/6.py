from functools import reduce
from itertools import chain

n = int(input())
print((max(list(map(
    max,
    reduce(
        lambda a, k: reduce(
            lambda a, i: reduce(
                lambda a, j: list(chain(
                    a[:i],
                    [list(chain(
                        a[i][:j],
                        [min(a[i][j], a[i][k] + a[k][j])],
                        a[i][j + 1:],
                    ))],
                    a[i + 1:],
                )),
                list(range(n)),
                a,
            ),
            list(range(n)),
            a,
        ),
        list(range(n)),
        list([list(map(int, input().split())) for i in range(n)])))))))

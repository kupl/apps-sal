"""
Codeforces Round #332

Problem 599 B. Spongebob and Joke

@author yamaton
@date 2015-11-20
"""


def solve(fs, bs, n, m):
    set_fs = set(fs)
    set_bs = set(bs)
    if not all(b in set_fs for b in bs):
        return ('Impossible', )

    # if len(bs) != len(set_bs):
    #     return ('Ambiguity', )

    ys = [f for f in fs if f in set_bs]
    if len(ys) != len(set(ys)):
        return ('Ambiguity',)

    d = {f: i for (i, f) in enumerate(fs, 1) if f in set_bs}
    return ('Possible', [d[b] for b in bs])


# def p(*args, **kwargs):
#     return print(*args, file=sys.stderr, **kwargs)


def main():
    [n, m] = list(map(int, input().strip().split()))
    fs = [int(_c) for _c in input().strip().split()]
    bs = [int(_c) for _c in input().strip().split()]
    assert len(fs) == n
    assert len(bs) == m

    result = solve(fs, bs, n, m)

    if len(result) == 1:
        print(result[0])
    else:
        print(result[0])
        print(*result[1])


def __starting_point():
    main()


__starting_point()

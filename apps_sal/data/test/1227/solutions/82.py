from sys import setrecursionlimit
setrecursionlimit(10 ** 6)
MAXN = 100

n = input()
k = int(input())

dl = [[None] * (MAXN + 1) for _ in range(MAXN + 1)]
de = [[None] * (MAXN + 1) for _ in range(MAXN + 1)]


def n_num_e(d, i):
    # d: n of digits
    # i: n of nonzero digits
    if d == 0:
        if i == 0:
            return 1
        else:
            return 0
    elif de[d][i] is not None:
        return de[d][i]
    else:
        if int(n[d - 1]) == 0:
            result = n_num_e(d - 1, i)
        else:
            result = n_num_e(d - 1, i - 1)
        de[d][i] = result
        return result


def n_num_l(d, i):
    # d: n of digits
    # i: n of nonzero digits
    if d == 0:
        return 0
    elif dl[d][i] is not None:
        return dl[d][i]
    else:
        if int(n[d - 1]) == 0:
            ne = 0
            nl = 9 * n_num_l(d - 1, i - 1) + n_num_l(d - 1, i)
            result = ne + nl
        else:
            ne = (int(n[d - 1]) - 1) * n_num_e(d - 1, i - 1) + n_num_e(d - 1, i)
            nl = 9 * n_num_l(d - 1, i - 1) + n_num_l(d - 1, i)
            result = ne + nl

        dl[d][i] = result
        return result


answer = n_num_e(len(n), k) + n_num_l(len(n), k)
print(answer)

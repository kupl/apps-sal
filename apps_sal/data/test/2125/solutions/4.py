import os
from io import BytesIO, StringIO
DEBUG = True
debug_print = print if DEBUG else lambda *x, **y: None


def input_as_list():
    return list(map(int, input().split()))


def array_of(f, *dim):
    return [array_of(f, *dim[1:]) for _ in range(dim[0])] if dim else f()


def main():
    (n, m) = input_as_list()
    g = [input() for _ in range(n)]
    prev_flgs = dict()
    s = 0
    for j in range(m):
        lst = []
        prev = ''
        cnt = 0
        for i in range(n):
            e = g[i][j]
            if e == prev:
                cnt += 1
            else:
                if prev:
                    lst.append((prev, cnt))
                prev = e
                cnt = 1
        lst.append((e, cnt))
        flgs = dict()
        idx = 0
        for i in range(len(lst) - 2):
            (f1, f2, f3) = (lst[i], lst[i + 1], lst[i + 2])
            if f1[1] == f2[1] == f3[1]:
                flgs[idx] = [f1[0] + f2[0] + f3[0], f1[1], 1]
            elif min(f1[1], f2[1], f3[1]) == f2[1]:
                flgs[idx + f1[1] - f2[1]] = [f1[0] + f2[0] + f3[0], f2[1], 1]
            idx += f1[1]
        if prev_flgs:
            for f in flgs:
                if f in prev_flgs:
                    fv = flgs[f]
                    pfv = prev_flgs[f]
                    if fv[0] == pfv[0] and fv[1] == pfv[1]:
                        s += pfv[2] + 1
                        flgs[f][2] = pfv[2] + 1
                    else:
                        s += 1
                else:
                    s += 1
        else:
            s += len(flgs)
        prev_flgs = flgs
    print(s)


main()

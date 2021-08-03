import sys
import math as m


def sort(a):
    mid = m.ceil(len(a) / 2)
    if len(a) == 1:
        return a
    else:
        al = sort(a[:mid])
        ar = sort(a[mid:])
        i = 0
        j = 0
        sa = []
        c = []
        while i < len(al) or j < len(ar):
            if i == len(al):
                sa.append(ar[j])
                j += 1
            elif j == len(ar):
                sa.append(al[i])
                i += 1
            elif al[i] > ar[j]:
                sa.append(ar[j])
                j += 1
            else:
                sa.append(al[i])
                i += 1
        return sa


def main():
    input = sys.stdin.readline()
    n = int(input)
    x = []
    y = []
    for i in range(4 * n + 1):
        input = sys.stdin.readline()
        X, Y = [int(j) for j in input.split()]
        x.append(X)
        y.append(Y)
    xs = sort(x)
    ys = sort(y)
    px = 0
    py = 0
    if xs[0] != xs[1]:
        X = xs[0]
    elif xs[4 * n - 1] != xs[4 * n]:
        X = xs[4 * n]
    else:
        px = 1
    if ys[0] != ys[1]:
        Y = ys[0]
    elif ys[4 * n - 1] != ys[4 * n]:
        Y = ys[4 * n]
    else:
        py = 1
    if px and not(py):
        i = 0
        while i < 4 * n + 1 and y[i] != Y:
            i += 1
        X = x[i]
    if py and not(px):
        i = 0
        while i < 4 * n + 1 and x[i] != X:
            i += 1
        Y = y[i]
    if px and py:
        i = 0
        while x[i] == min(x) or x[i] == max(x) or y[i] == min(y) or y[i] == max(y):
            i += 1
        X, Y = x[i], y[i]
    print(X, Y)


def __starting_point():
    main()


__starting_point()

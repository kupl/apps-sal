import sys


def main():
    n = int(sys.stdin.readline().rstrip())
    a = list(map(int, sys.stdin.readline().split()))
    b = list(map(int, sys.stdin.readline().split()))
    items = set(range(1, n + 1))
    coords = []
    p = [-1] * n
    for i in range(n):
        if a[i] == b[i]:
            items.remove(a[i])
            p[i] = a[i]
        else:
            coords.append(i)
    items = list(items)
    if len(coords) == 1:
        p[coords[0]] = items[0]
    else:
        adelta = 0
        bdelta = 0
        for (k, coord) in enumerate(coords):
            if items[k] != a[coord]:
                adelta += 1
            if items[k] != b[coord]:
                bdelta += 1
            p[coord] = items[k]
        if not (adelta == 1 and bdelta == 1):
            adelta = 0
            bdelta = 0
            for (k, coord) in enumerate(reversed(coords)):
                if items[k] != a[coord]:
                    adelta += 1
                if items[k] != b[coord]:
                    bdelta += 1
                p[coord] = items[k]
    sys.stdout.write(' '.join(map(str, p)) + '\n')


main()

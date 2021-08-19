from collections import defaultdict


def main():
    n = int(input())
    bydegree = defaultdict(set)
    bys = defaultdict(set)
    l = []
    for i in range(n):
        (degree, s) = list(map(int, input().split()))
        bydegree[degree].add(i)
        bys[s].add(i)
        l.append((degree, s))
    res = []
    ones = bydegree[1]
    while ones:
        i = ones.pop()
        (degree_i, j) = l[i]
        (degree_j, s) = l[j]
        res.append(' '.join((str(i), str(j))))
        bydegree[degree_j].remove(j)
        degree_j -= 1
        bydegree[degree_j].add(j)
        l[j] = (degree_j, s ^ i)
    print(len(res))
    print('\n'.join(res))


def __starting_point():
    main()


__starting_point()

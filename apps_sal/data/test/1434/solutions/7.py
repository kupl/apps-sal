def main():
    n = int(input())
    ones, l = set(), []
    for i in range(n):
        degree, s = list(map(int, input().split()))
        if degree == 1:
            ones.add(i)
        l.append((degree, s))
    res = []
    while ones:
        i = ones.pop()
        degree_i, j = l[i]
        degree_j, s = l[j]
        res.append(' '.join((str(i), str(j))))
        if degree_j == 1:
            ones.remove(j)
        else:
            degree_j -= 1
            if degree_j == 1:
                ones.add(j)
            l[j] = (degree_j, s ^ i)
    print(len(res))
    print('\n'.join(res))


def __starting_point():
    main()

__starting_point()

def __starting_point():
    n = int(input())
    d = input()
    w = [int(i) for i in input().split()]
    visited = set()
    i = 0
    while (i not in visited) and (i < n) and (i > -1):
        visited.add(i)
        if d[i] == '>':
            i += w[i]
        else:
            i -= w[i]
    if (i >= 0) and (i < n):
        print('INFINITE')
    else:
        print('FINITE')


__starting_point()

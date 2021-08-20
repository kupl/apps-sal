def qa():
    (n, k) = map(int, input().split())
    if k > n:
        print('-1')
        return
    matrix = [[0] * n for _ in range(n)]
    for i in range(k):
        matrix[i][i] = 1
    for line in matrix:
        print(' '.join(map(str, line)))


def qb():
    _ = input()
    d = [*map(int, input().split())]
    zeroIndex = [0 if v == 0 else len(d) for (i, v) in enumerate(d)]
    counter = len(d)
    for i in range(len(d)):
        if zeroIndex[i] == 0:
            counter = 0
            continue
        counter += 1
        zeroIndex[i] = min(counter, zeroIndex[i])
    counter = len(d)
    for i in range(len(d) - 1, -1, -1):
        if zeroIndex[i] == 0:
            counter = 0
            continue
        counter += 1
        zeroIndex[i] = min(counter, zeroIndex[i])
    print(' '.join(map(str, zeroIndex)))


qb()

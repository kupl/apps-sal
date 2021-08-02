def increasing(m):
    for i in range(len(m)):
        prev = m[i][0]
        for j in range(1, len(m[i])):
            if m[i][j] <= prev: return False
            prev = m[i][j]
    for j in range(len(m[0])):
        prev = m[0][j]
        for i in range(1, len(m)):
            if m[i][j] <= prev: return False
            prev = m[i][j]
    return True


def sol(m1, m2):
    for i in range(len(m1)):
        for j in range(len(m1[i])):
            if m1[i][j] > m2[i][j]:
                m1[i][j], m2[i][j] = m2[i][j], m1[i][j]
    if not increasing(m1) or not increasing(m2): return 'Impossible'
    return 'Possible'


def __starting_point():
    [n, m] = [int(x) for x in input().split()]
    m1, m2 = [], []
    for _ in range(n): m1.append([int(x) for x in input().split()])
    for _ in range(n): m2.append([int(x) for x in input().split()])
    print(sol(m1, m2))


__starting_point()

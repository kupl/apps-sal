data = []
face = set({'f', 'a', 'c', 'e'})


def check(data, i, j):
    s = set()
    s.add(data[i][j])
    s.add(data[i + 1][j])
    s.add(data[i + 1][j + 1])
    s.add(data[i][j + 1])

    if len(s & face) == 4:
        return True

    return False


def __starting_point():
    n, m = map(int, input().split())

    for i in range(n):
        data.append(input())

    total = 0
    for i in range(n - 1):
        for j in range(m - 1):
            if check(data, i, j):
                total += 1

    print(total)


__starting_point()

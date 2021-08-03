com = [[0] * 19 for i in range(19)]


def solve(x):
    sx, non_zero, res = str(x), 3, 0

    for i in range(len(sx)):
        if not int(sx[i]):
            continue

        for j in range(0, non_zero + 1):
            res += com[len(sx) - i - 1][j] * 9 ** j

        non_zero -= 1

        if non_zero == -1:
            break

        for j in range(0, non_zero + 1):
            res += (int(sx[i]) - 1) * com[len(sx) - i - 1][j] * 9 ** j

    return res


def main():
    t = int(input())

    for i in range(19):
        com[i][0] = 1
    for i in range(1, 19):
        for j in range(1, i + 1):
            com[i][j] = com[i - 1][j] + com[i - 1][j - 1]

    for i in range(t):
        l, r = list(map(int, input().split()))
        print(solve(r + 1) - solve(l))


def __starting_point():
    main()


__starting_point()

def simulate(n, m, first, last, mask):
    pos = 'left'
    time = 0

    for floor in range(n - 1):
        action = mask & 1
        mask >>= 1

        if pos == 'left':
            if action == 0:
                time += 2 * last[floor]
            else:
                time += m + 1
                pos = 'right'
        else:
            if action == 0:
                time += 2 * (m + 1 - first[floor])
            else:
                time += m + 1
                pos = 'left'

        time += 1

    if pos == 'left':
        time += last[n - 1]
    else:
        time += m + 1 - first[n - 1]

    return time


def main():
    n, m = list(map(int, input().split()))

    building = []
    for i in range(n):
        building.append(list(map(int, input())))

    i_max = None
    for i in range(n):
        if any(x == 1 for x in building[i]):
            i_max = i
            break

    if i_max is None:
        i_max = n
    n = n - i_max

    if n == 0:
        print(0)
        return

    building = building[::-1]
    building = building[:n]

    first = [m + 1] * n
    last = [0] * n

    for i in range(n):
        for j in range(m + 2):
            if building[i][j] == 1:
                if first[i] == m + 1:
                    first[i] = j
                last[i] = j

    min_time = 10 * ((m + 1) * n + n)
    for mask in range(2 ** (n - 1)):
        min_time = min(min_time, simulate(n, m, first, last, mask))

    print(min_time)


def __starting_point():
    main()


__starting_point()

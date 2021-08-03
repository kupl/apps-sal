def main():
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    month2day = {}
    cnt = 0
    for i in range(9, 12 + 1):
        for j in range(1, days_in_month[i - 1] + 1):
            month2day[(i, j, 12)] = cnt
            cnt += 1

    for i in range(1, 12 + 1):
        for j in range(1, days_in_month[i - 1] + 1):
            month2day[(i, j, 13)] = cnt
            cnt += 1

    with open('input.txt') as f:
        test = f.readlines()

    n = int(test[0].strip())

    days = [0] * len(month2day)
    for i in range(1, n + 1):
        m, d, p, t = map(int, test[i].strip().split())
        R = month2day[(m, d, 13)] - 1
        L = R - t + 1
        days[L] += p
        days[R + 1] -= p

    acc = [days[0]]
    for i in range(1, len(days)):
        acc.append(acc[-1] + days[i])

    with open('output.txt', 'w') as f:
        f.write(str(max(acc)))


def __starting_point():
    main()


__starting_point()

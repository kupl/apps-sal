def read():
    n, k = list(map(int, input().split()))
    powers = list(map(int, input().split()))
    return n, k, powers


def get_min_power(n, k, powers):
    start_task = 0
    mins = []
    for i in range(k):
        s = 0
        for j in range(i, n, k):
            s += powers[j]
        mins.append(s)
    task = min(mins)
    return mins.index(task) + 1


def main():
    n, k, powers = read()
    print(get_min_power(n, k, powers))


def __starting_point():
    main()


__starting_point()

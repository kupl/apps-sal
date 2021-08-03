def find_smallest(fx, allow_nine_end):
    if fx < 0:
        return None

    if fx == 0:
        return ""

    a = []
    if not allow_nine_end:
        d = min(8, fx)
        a.append(d)
        fx -= d
    while fx:
        d = min(9, fx)
        a.append(d)
        fx -= d
    return "".join(map(str, a[::-1]))


t = int(input())

for _ in range(t):
    n, k = list(map(int, input().split()))

    m = 10**20

    for end in range(0, 9 - k + 1):
        a = n - k * (k + 1) // 2
        if a % (k + 1) != 0:
            continue
        fx = a // (k + 1)
        f = find_smallest(fx - end, True)
        if f is not None:
            m = min(m, int(str(f) + str(end)))

    for flips in range(1, 20):
        for count_after_flip in range(1, k + 1):
            a = n + 9 * flips * count_after_flip - k * (k + 1) // 2
            if a % (k + 1) != 0:
                continue
            fx = a // (k + 1)
            end = count_after_flip - k - 1 + 10
            nines_count = flips - 1

            f = find_smallest(fx - end - 9 * nines_count, False)
            if f is not None:
                m = min(m, int(str(f) + "9" * nines_count + str(end)))

    if m != 10**20:
        print(m)
    else:
        print(-1)

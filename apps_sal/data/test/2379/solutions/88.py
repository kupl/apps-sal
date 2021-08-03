def main():
    n, k, c = list(map(int, input().split()))
    s = input()
    schedule = [w == "o" for w in s]
    left = []
    l_day = 0
    right = []
    r_day = n - 1
    while len(left) < k:
        if schedule[l_day]:
            left.append(l_day)
            l_day += c
        l_day += 1

    while len(right) < k:
        if schedule[r_day]:
            right.append(r_day)
            r_day -= c
        r_day -= 1

    right.reverse()

    for i in range(k):
        if left[i] == right[i]:
            print((left[i] + 1))


def __starting_point():
    main()


__starting_point()

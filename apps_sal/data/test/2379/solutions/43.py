def main() -> None:
    (n, k, c) = list(map(int, input().split()))
    s = input()
    if k < s.count('o') and c == 0:
        print('')
        return
    count = c
    (day_work, day_work_reverse) = ([], [])
    for (i, day) in enumerate(s):
        count += 1
        if day == 'o' and c < count:
            day_work.append(i + 1)
            count = 0
    count = c
    for (i, day) in enumerate(s[::-1]):
        count += 1
        if day == 'o' and c < count:
            day_work_reverse.append(n - i)
            count = 0
    day_must = set(day_work[:k]) & set(day_work_reverse[:k])
    for day in sorted(list(day_must)):
        print(day)
    return


def __starting_point():
    main()


__starting_point()

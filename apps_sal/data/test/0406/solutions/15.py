def main():
    n = int(input())
    l = [int(i) for i in input().split()]
    l.sort()
    l.reverse()
    candidate = []
    i = 1
    while i < n:
        if l[i - 1] - l[i] <= 1:
            candidate.append(min(l[i - 1], l[i]))
            i += 2
        else:
            i += 1
    area = 0
    for i in range(1, len(candidate), 2):
        area += candidate[i] * candidate[i - 1]
    return area


def __starting_point():
    print(main())


__starting_point()

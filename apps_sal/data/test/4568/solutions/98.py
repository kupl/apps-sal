def calc_intersection():
    n = int(input())
    s = input()
    list_intersection = []
    for i in range(1, n):
        a = set(s[:i])
        b = set(s[i:])
        intersection_a_b = a.intersection(b)
        list_intersection.append(len(intersection_a_b))
    return max(list_intersection)


def __starting_point():
    print(calc_intersection())


__starting_point()

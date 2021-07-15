def diff_list_max(l: list) -> int:
    return abs(max(l) - min(l))


def __starting_point():
    n = int(input())
    l = list(map(int, input().split()))
    print((diff_list_max(l)))

__starting_point()

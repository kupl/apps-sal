def generate_polygon(length: list) -> str:
    length.sort()
    len_max = length.pop()
    len_sum = sum(length)
    if len_max < len_sum:
        return "Yes"
    return "No"


def __starting_point():
    n = int(input())
    length = list(map(int, input().split()))
    print((generate_polygon(length)))


__starting_point()

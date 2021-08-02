def view_check(n: int, heights: list) -> int:
    cnt = 1
    max_height = heights[0]
    for i in range(1, n):
        if heights[i] >= max_height:
            cnt += 1
            max_height = heights[i]
    return cnt


def __starting_point():
    n = int(input())
    heights = list(map(int, input().split()))
    print((view_check(n, heights)))


__starting_point()

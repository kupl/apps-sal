def main():
    x = int(input())
    start = 100
    cnt = 0
    while start < x:
        start += start // 100
        cnt += 1
    return cnt


def __starting_point():
    print((main()))

__starting_point()

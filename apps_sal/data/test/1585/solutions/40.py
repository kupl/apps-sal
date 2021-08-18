
def resolve():
    import sys
    input = sys.stdin.readline

    x, y = [int(x) for x in input().rstrip().split(" ")]

    count = 1
    num = x
    while num * 2 <= y:
        count += 1
        num *= 2
    print(count)


def __starting_point():
    resolve()


__starting_point()

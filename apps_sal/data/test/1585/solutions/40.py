# row = [int(x) for x in input().rstrip().split(" ")]
# n = int(input().rstrip())
# s = input().rstrip()
# row = [int(input().rstrip()) for _ in range(n)]

def resolve():
    import sys
    input = sys.stdin.readline

    x, y = [int(x) for x in input().rstrip().split(" ")]

    # 2 ** ?
    count = 1
    num = x
    while num * 2 <= y:
        count += 1
        num *= 2
    print(count)


def __starting_point():
    resolve()


__starting_point()

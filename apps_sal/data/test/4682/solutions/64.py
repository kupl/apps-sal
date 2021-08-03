def solve(a, b, h):
    ans = (a + b) * h // 2
    return ans


def __starting_point():
    a = int(input())
    b = int(input())
    h = int(input())
    print((solve(a, b, h)))


__starting_point()

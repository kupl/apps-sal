def calc(n, m):
    holidays = n
    a = list(int(v) for v in input().split())
    ans = holidays - sum(a)
    return ans if ans >= 0 else -1


def main():
    n, m = list(map(int, input().split()))
    return calc(n, m)


def __starting_point():
    print((main()))

__starting_point()

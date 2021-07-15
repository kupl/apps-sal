def solve(inp):
    c, v0, v1, a, l = list(map(int, inp.split(" ", 4)))
    pages_read = 0
    days_passed = 0
    while pages_read < c:
        pages_read += v0 - min(l, pages_read)
        days_passed += 1
        v0 = min(v0 + a, v1)
    return days_passed


def __starting_point():
    print(solve(input()))

__starting_point()

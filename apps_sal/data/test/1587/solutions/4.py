def solve(string):
    _, c = string.split()
    r = c.count("R")
    return str(c[:r].count("W"))


def __starting_point():
    import sys
    print((solve(sys.stdin.read().strip())))


__starting_point()

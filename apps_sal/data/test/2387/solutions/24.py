def check(vec):
    if len(vec) == 0:
        return True
    h = 0
    for v in sorted(vec, reverse=True):
        if h + v[0] < 0:
            return False
        h += v[1]
    return True


def parse(brackets):
    m = 0
    f = 0
    for c in brackets:
        if c == "(":
            f += 1
        else:
            f -= 1
        if m > f:
            m = f
    return m, f


def main():
    N = int(input())
    ls = []
    rs = []
    tot = 0
    for _ in range(N):
        m, f = parse(input().strip())
        tot += f
        if f >= 0:
            ls.append([m, f])
        else:
            rs.append([m - f, -f])
    return tot == 0 and check(ls) and check(rs)


def __starting_point():
    print(("Yes" if main() else "No"))


__starting_point()

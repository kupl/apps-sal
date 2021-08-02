def main():
    a, b = list(map(int, input().split()))
    f = str(a) * b
    s = str(b) * a
    ans = [f, s]
    ans.sort()
    return ans[0]


def __starting_point():
    print((main()))


__starting_point()

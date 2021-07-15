"""http://codeforces.com/problemset/problem/233/B"""

def s(x): return sum(map(int, str(x)))
def solve(n):
    l = 1; r = int(n ** 0.5); max_s = 81
    for x in range(max(1, r - max_s), r + 1):
        if x * (x + s(x)) == n:
            return x
    return -1

def test():
    assert solve(2) == 1
    assert solve(110) == 10
    assert solve(4) == -1
    assert solve(10000006999999929) == 99999999


def __starting_point():
    test()
    print(solve(int(input())))

__starting_point()

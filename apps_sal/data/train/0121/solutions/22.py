def solve(n, a_s):
    a_s.sort()
    return a_s[n] - a_s[n - 1]


def __starting_point():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a_s = [int(ch) for ch in input().split(' ')]
        print(solve(n, a_s))

__starting_point()

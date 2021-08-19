def solve(n, a):
    max_p = 0
    ans = 0
    for (p, ai) in enumerate(a):
        if ai > max_p:
            max_p = ai
        if p == max_p:
            ans += 1
    return ans


def __starting_point():
    n = int(input())
    a = [int(p) - 1 for p in input().split()]
    print(solve(n, a))


__starting_point()

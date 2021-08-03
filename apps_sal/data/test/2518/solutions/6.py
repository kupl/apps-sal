def binsearch(good, bad, fn):
    while abs(good - bad) > 1:
        m = (good + bad) // 2
        if fn(m):
            good = m
        else:
            bad = m
    return good


def main():
    N, A, B = list(map(int, input().split()))
    H = [int(input()) for _ in range(N)]
    c = A - B

    def helper(x):
        r = 0
        for h in H:
            r += max((h - B * x + c - 1) // c, 0)
        return r <= x

    return binsearch(10**9, 0, helper)


print((main()))

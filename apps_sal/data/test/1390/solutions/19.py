import random


def solve(l, n, m):
    sl = sorted(l)
    # print(sl)
    return min([sl[i + n - 1] - sl[i] for i in range(m - n + 1)])


def test():
    assert solve([9, 2], 2, 2) == 7
    assert solve([4, 4], 2, 2) == 0
    assert solve([9, 2, 4, 4], 2, 4) == 0
    assert solve([10, 12, 10, 7, 5, 22], 4, 6) == 5
    assert solve([1, 5, 2, 19], 2, 4) == 1
    print("test passes")


n, m = list(map(int, input().split()))
l = list(map(int, input().split()))
print(solve(l, n, m))
# test()

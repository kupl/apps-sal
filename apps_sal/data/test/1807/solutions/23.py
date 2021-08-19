def proc(x, nums):
    res = 0
    while x != 0:
        res += nums[x % 10]
        x //= 10
    return res


def __starting_point():
    nums = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
    (a, b) = [int(x) for x in input().split()]
    res = 0
    s = str(list(range(a, b + 1)))
    for i in range(10):
        res += nums[i] * s.count(str(i))
    print(res)


__starting_point()

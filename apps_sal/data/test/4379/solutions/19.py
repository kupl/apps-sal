from collections import Counter


def read_nums():
    return [int(x) for x in input().split()]


def main():
    (n,) = read_nums()
    nums = read_nums()
    dp = Counter()
    for i in range(n):
        dp[nums[i]] = dp[nums[i] - 1] + 1
    indexes = {}
    for i in range(n):
        indexes[nums[i]] = i
    last_num = max(list(dp.items()), key=lambda x: x[1])[0]
    result = []
    for i in range(n - 1, -1, -1):
        if nums[i] == last_num:
            result.append(i)
            last_num -= 1
    result.reverse()
    print(len(result))
    print(' '.join([str(x + 1) for x in result]))


def __starting_point():
    main()


__starting_point()

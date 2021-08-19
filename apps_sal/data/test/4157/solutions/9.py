from collections import Counter


def read_nums():
    return [int(x) for x in input().split()]


def solve(res, num, c, n):
    res.append(num)
    c[num] -= 1
    if n == 0:
        print(' '.join([str(x) for x in res]))
        return
    if num % 3 == 0 and num // 3 in c:
        solve(res, num // 3, c, n - 1)
        res.pop()
        c[num // 3] += 1
    if num * 2 in c:
        solve(res, num * 2, c, n - 1)
        res.pop()
        c[num * 2] += 1


def main():
    n = int(input())
    nums = read_nums()
    c = Counter(nums)
    res = []
    for num in nums:
        solve(res, num, c, n - 1)
        res.pop()
        c[num] += 1


def __starting_point():
    main()


__starting_point()

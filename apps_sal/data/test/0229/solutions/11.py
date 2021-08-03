def solve():
    input()
    a = list(map(int, input().split()))
    nums = set()
    for n in a:
        nums.add(n)

    if len(nums) <= 2:
        print('YES')
        return

    if len(nums) == 3:
        ma = max(nums)
        mi = min(nums)
        nums.remove(ma)
        nums.remove(mi)
        mid = nums.pop()
        if ma - mid == mid - mi:
            print('YES')
            return

    print('NO')


def main():
    solve()


def __starting_point():
    main()


__starting_point()

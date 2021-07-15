from collections import Counter


def solve(nums):
    c = Counter(nums)
    if c[2] == 0:
        return ' '.join(map(str, [1 for _ in range(c[1])]))
    elif c[1] == 0:
        return ' '.join(map(str, [2 for _ in range(c[2])]))
    else:
        output = [2, 1]
        c[2] -= 1
        c[1] -= 1
        if c[2] > 0:
            output.extend([2 for _ in range(c[2])])
        if c[1] > 0:
            output.extend([1 for _ in range(c[1])])
        return ' '.join(map(str, output))


def main():
    _ = int(input())
    nums = list(map(int, input().split()))
    print(solve(nums))


def __starting_point():
    main()

__starting_point()

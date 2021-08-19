from collections import deque


def main():
    from sys import stdin
    lines = deque(line.strip() for line in stdin.readlines())
    # lines will now contain all of the input's lines in a list
    n = int(lines[0])
    nums = sorted(int(x) for x in lines[1].split())
    for i in range(2, n):
        if nums[i - 2] + nums[i - 1] > nums[i]:
            print("YES")
            return
    print("NO")


def __starting_point():
    main()


__starting_point()

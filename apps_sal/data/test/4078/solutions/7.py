def read_nums():
    return [int(x) for x in input().split()]


def calculate_diff(i1, i2, nums, all_segments):
    cur_diff = nums[i2] - nums[i1]
    used_segments = []
    for index, segment in enumerate(all_segments):
        left, right = segment
        if left <= i1 <= right and not (left <= i2 <= right):
            used_segments.append(index)
            cur_diff += 1
    return cur_diff, used_segments


def main():
    n, m = read_nums()
    nums = read_nums()
    segments = [[x - 1 for x in read_nums()] for _ in range(m)]

    if n == 1:
        print(0)
        print(0)
        return

    candidates = []
    for i1, num1 in enumerate(nums):
        for i2, num2 in enumerate(nums):
            if i1 == i2:
                continue
            diff, used_segments = calculate_diff(i1, i2, nums, segments)
            candidates.append((diff, used_segments))

    res_diff, segment_indexes = max(candidates, key=lambda x: x[0])
    print(res_diff)
    print(len(segment_indexes))
    if len(segment_indexes) > 0:
        print(' '.join([str(x + 1) for x in segment_indexes]))


def __starting_point():
    main()


__starting_point()

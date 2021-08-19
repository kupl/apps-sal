#! /usr/bin/env python3
import bisect


def memo(f):
    def _f(*args):
        key = str(args)
        try:
            return cache[key]
        except KeyError:
            data = cache[key] = f(*args)
            return data
    cache = {}
    return _f


@memo
def count_inversions(nums):
    invs = 0
    for i, lnum in enumerate(nums):
        for rnum in nums[i + 1:]:
            if lnum > rnum:
                invs += 1
    return invs


def search(depth, nums):
    if depth >= max_depth:
        return count_inversions(nums), 1
    else:
        invs = total = 0
        depth += 1
        for i in range(length):
            for j in range(i + 1, length + 1):
                nums[i:j] = nums[i:j][::-1]
                invs, total = list(map(sum, list(zip(search(depth, nums), (invs, total)))))
                nums[i:j] = nums[i:j][::-1]
        return invs, total


length, max_depth = list(map(int, input().split()))
nums = list(map(int, input().split()))
invs, total = search(0, nums)
print(invs / total)

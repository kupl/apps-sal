#! /usr/bin/env python3

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

def count_inversions(lo, hi):
    if hi - lo <= 1:
        return 0, nums[lo:hi]
    mid = (lo + hi) // 2
    invs, (nums1, nums2) = list(zip(count_inversions(lo, mid), count_inversions(mid, hi)))
    invs = sum(invs)
    new_nums = []
    i1 = i2 = 0
    l1, l2 = list(map(len, (nums1, nums2)))
    for _ in range(l1 + l2):
        if i1 == l1:
            new_nums.append(nums2[i2])
            i2 += 1
        elif i2 == l2:
            new_nums.append(nums1[i1])
            i1 += 1
        elif nums1[i1] <= nums2[i2]:
            new_nums.append(nums1[i1])
            i1 += 1
        else:
            new_nums.append(nums2[i2])
            i2 += 1
            invs += l1 - i1
    return invs, new_nums

# def count_inversions(lo, hi):
#     invs = 0
#     for i in range(len(nums)):
#         for j in range(i, len(nums)):
#             if nums[i] > nums[j]:
#                 invs += 1
#     return invs, 0

@memo
def search(depth, nums):
    if depth >= max_depth:
        invs, _ = count_inversions(0, len(nums))
        return invs, 1
    else:
        invs = total = 0
        depth += 1
        for i in range(length):
            for j in range(i + 1, length + 1):
                nums[i:j] = nums[i:j][::-1]
                invs, total = list(map(sum, list(zip(search(depth, nums), (invs, total)))))
                nums[i:j] = nums[i:j][::-1]
        return invs, total

MAX = 1e9

length, max_depth = list(map(int, input().split()))
nums = list(map(int, input().split()))
invs, total = search(0, nums)
print(invs / total)



def func(xs, ys):
    sqs = [x**2 for x in xs]
    seen = collections.defaultdict(int)
    res = 0
    for y in ys:
        for x in sqs:
            res += seen[x / y]
        seen[y] += 1

    return res


class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        return func(nums1, nums2) + func(nums2, nums1)

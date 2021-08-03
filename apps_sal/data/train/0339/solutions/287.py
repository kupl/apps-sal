from bisect import bisect_right
from collections import defaultdict


def sol(inp1, inp2):
    values1 = defaultdict(list)
    values2 = defaultdict(list)
    inp1.sort()
    inp2.sort()
    for i1, v1 in enumerate(inp1):
        values1[v1].append(i1)
    for i2, v2 in enumerate(inp2):
        values2[v2].append(i2)
    count = 0
    for i1, v1 in enumerate(inp1):
        for i2, v2 in enumerate(inp2):
            if v2 > v1:
                break
            matches = values2[(v1 * v1) / v2]
            ins = bisect_right(matches, i2)
            count += len(matches) - ins
    for i2, v2 in enumerate(inp2):
        for i1, v1 in enumerate(inp1):
            if v1 > v2:
                break
            matches = values1[(v2 * v2) / v1]
            ins = bisect_right(matches, i1)
            count += len(matches) - ins
    return count


class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        return sol(nums1, nums2)

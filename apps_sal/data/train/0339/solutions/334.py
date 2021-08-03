from collections import Counter


class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        counter1 = Counter(nums1)
        counter2 = Counter(nums2)

        ret = 0
        for k, v in counter1.items():
            for i in range(1, k):
                if i in counter2 and k * k / i in counter2:
                    ret += v * counter2[i] * counter2[k * k / i]
            if counter2[k] >= 2:
                ret += v * counter2[k] * (counter2[k] - 1) / 2

        for k, v in counter2.items():
            for i in range(1, k):
                if i in counter1 and k * k / i in counter1:
                    ret += v * counter1[i] * counter1[k * k / i]
            if counter1[k] >= 2:
                ret += v * counter1[k] * (counter1[k] - 1) / 2
        return int(ret)

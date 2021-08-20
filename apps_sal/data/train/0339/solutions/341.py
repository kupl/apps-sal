class Solution:

    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:

        def helper(target, nums):
            ret = 0
            target = target * target
            d = {}
            s = set()
            for n in nums:
                if n in d:
                    s.add((min(n, target // n), max(n, target // n)))
                if target % n == 0:
                    if target // n in d:
                        d[target // n] += 1
                    else:
                        d[target // n] = 1
            for (a, b) in s:
                if a == b:
                    ret += d[a] * (d[a] - 1) // 2
                else:
                    ret += d[a] * d[b]
            return ret
        ans = 0
        for n1 in nums1:
            ans += helper(n1, nums2)
        for n2 in nums2:
            ans += helper(n2, nums1)
        return ans

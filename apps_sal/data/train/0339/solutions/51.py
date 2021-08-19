class Solution:

    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        num1_counts = collections.Counter(nums1)
        num2_counts = collections.Counter(nums2)
        res = 0

        def findMatches(d1, d2):
            res = 0
            for n1 in d1:
                square = n1 * n1
                checked = set()
                for n2 in d2:
                    if n2 in checked or square % n2:
                        continue
                    k = square // n2
                    if k == n2:
                        res += d1[n1] * d2[n2] * (d2[n2] - 1) // 2
                    elif k in d2:
                        res += d1[n1] * d2[n2] * d2[k]
                        checked.add(k)
                    checked.add(n2)
            return res
        return findMatches(num1_counts, num2_counts) + findMatches(num2_counts, num1_counts)

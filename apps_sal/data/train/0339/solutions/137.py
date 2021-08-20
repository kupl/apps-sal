class Solution:

    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:

        def count(n1, n2):
            l2 = len(n2)
            cnt = Counter()
            for k in range(l2):
                for j in range(k):
                    v = n2[k] * n2[j]
                    cnt[v] += 1
            ans = 0
            for x in n1:
                ans += cnt[x * x]
            return ans
        return count(nums1, nums2) + count(nums2, nums1)

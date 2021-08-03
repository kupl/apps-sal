class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        fin = 0

        for n in nums1:
            sq = n * n
            res = {}
            ans = defaultdict(list)

            for i, x in enumerate(nums2):
                y = sq / x

                if y in ans:
                    fin += len(ans[y])
                ans[x].append(i)

        for n in nums2:
            sq = n * n
            res = set()
            ans = defaultdict(list)

            for i, x in enumerate(nums1):
                y = sq / x

                if y in ans:
                    fin += len(ans[y])
                ans[x].append(i)

        return fin

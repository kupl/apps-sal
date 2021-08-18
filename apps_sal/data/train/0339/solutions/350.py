class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        ans = 0

        def helper(l1, l2):
            nonlocal ans
            c = Counter(l2)
            for x in l1:
                num = x * x
                c2 = c.copy()
                for i in range(len(l2)):
                    curr = l2[i]
                    c2[curr] -= 1
                    if c2[curr] == 0:
                        c2.pop(curr)
                    if num % curr == 0 and num // l2[i] in c2:
                        ans += c2[num // l2[i]]

        helper(nums1, nums2)
        helper(nums2, nums1)
        return ans

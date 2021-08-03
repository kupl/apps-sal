class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        # all positive numbers

        #         nums1.sort()
        #         nums2.sort()

        #         d1 = {}
        #         d2 = {}

        #         self.ret = 0
        #         def helper(a, b):
        #             # pick one from a and pick two from b, record products in d
        #             if len(b) < 2:
        #                 return
        #             # print(a, b)
        #             for n in a:
        #                 # iterate through a
        #                 # n ^ 2 = product of two numbers in b
        #                 for i in range(len(b)-1):
        #                     if n * n > b[i] * b[-1]:
        #                         continue
        #                     for j in range(i+1, len(b)):
        #                         if n * n == b[i] * b[j]:
        #                             # found pairs
        #                             self.ret += 1
        #                         elif n * n < b[i] * b[j]:
        #                             break

        #         helper(nums1, nums2)
        #         helper(nums2, nums1)

        # return self.ret

        def helper(target, nums):
            ret = 0
            target = target * target
            d = {}
            s = set()
            for n in nums:
                if n in d:
                    # there is a pair
                    s.add((min(n, target // n), max(n, target // n)))

                if target % n == 0:
                    # candidate
                    if target // n in d:
                        d[target // n] += 1
                    else:
                        d[target // n] = 1

            # print(target, nums, s, d)
            for a, b in s:
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

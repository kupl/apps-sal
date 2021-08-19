class Solution:

    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        def twoProduct(n, nums):
            counter = collections.Counter()
            res = 0
            for num in nums:
                if n % num == 0:
                    res += counter[n / num]
                counter[num] += 1
            return res
        res = 0
        for num in nums1:
            res += twoProduct(num * num, nums2)
        for num in nums2:
            res += twoProduct(num * num, nums1)
        return res


#         res = 0
#         d1 = collections.defaultdict(list)
#         for i, num in enumerate(nums1):
#             d1[num].append(i)

#         for i in range(len(nums2) - 1):
#             for j in range(i+1, len(nums2)):
#                 sqrt = (nums2[i]*nums2[j])**0.5
#                 if sqrt == int(sqrt) and sqrt in d1:
#                     res += len(d1[sqrt])
#         d2 = collections.defaultdict(list)
#         for i, num in enumerate(nums2):
#             d2[num].append(i)

#         for i in range(len(nums1) - 1):
#             for j in range(i+1, len(nums1)):
#                 sqrt = (nums1[i]*nums1[j])**0.5
#                 if sqrt == int(sqrt) and sqrt in d2:
#                     res += len(d2[sqrt])
#         return res

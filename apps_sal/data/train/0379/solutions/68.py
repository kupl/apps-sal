class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        n1 = len(nums1)
        n2 = len(nums2)

        a1 = [-1 for _ in range(n1)]
        a2 = [-1 for _ in range(n2)]

        i, j = 0, 0
        while i < n1 and j < n2:
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                a1[i] = j
                a2[j] = i
                i += 1
                j += 1

        cache1 = {}
        cache2 = {}

        def process1(idx):
            if idx == n1:
                return 0
            if not idx in cache1:
                ans = 0
                if a1[idx] == -1:
                    ans = nums1[idx] + process1(idx + 1)
                else:
                    ans = nums1[idx] + max(process1(idx + 1), process2(a1[idx] + 1))
                cache1[idx] = ans
            return cache1[idx]

        def process2(idx):
            if idx == n2:
                return 0
            if not idx in cache2:
                ans = 0
                if a2[idx] == -1:
                    ans = nums2[idx] + process2(idx + 1)
                else:
                    ans = nums2[idx] + max(process2(idx + 1), process1(a2[idx] + 1))
                cache2[idx] = ans
            return cache2[idx]

        return max(process1(0), process2(0)) % (10 ** 9 + 7)

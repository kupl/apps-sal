class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        memo1 = defaultdict(lambda: 0)
        memo2 = defaultdict(lambda: 0)
        nums1.append(0)
        nums2.append(0)

        i = len(nums1) - 2
        j = len(nums2) - 2
        while i >= 0 or j >= 0:
            n1 = nums1[i] if i >= 0 else 0
            n2 = nums2[j] if j >= 0 else 0

            if n1 == n2:
                memo1[n1] = max(n1 + memo1[nums1[i + 1]], n2 + memo2[nums2[j + 1]])
                memo2[n2] = memo1[n1]
                i -= 1
                j -= 1
            elif n1 > n2:
                memo1[n1] = max(n1 + memo1[nums1[i + 1]], memo2[n1])
                i -= 1
            else:
                memo2[n2] = max(n2 + memo2[nums2[j + 1]], memo1[n2])
                j -= 1

        return max(memo1[nums1[0]], memo2[nums2[0]]) % int(1e9 + 7)

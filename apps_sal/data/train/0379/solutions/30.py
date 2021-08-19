class Solution:

    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        (n1, n2) = (nums1, nums2)
        (s, t, sum1, sum2) = (len(n1) - 1, len(n2) - 1, 0, 0)
        ans = 0
        while s >= 0 and t >= 0:
            if n1[s] > n2[t]:
                sum1 += n1[s]
                s -= 1
            elif n1[s] < n2[t]:
                sum2 += n2[t]
                t -= 1
            else:
                ans += max(sum1 + n1[s], sum2 + n1[s])
                sum1 = sum2 = 0
                s -= 1
                t -= 1
        if s >= 0:
            ans += max(sum1 + sum(n1[:s + 1]), sum2)
        if t >= 0:
            ans += max(sum1, sum2 + sum(n2[:t + 1]))
        return ans % (10 ** 9 + 7)

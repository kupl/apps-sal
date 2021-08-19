class Solution:

    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        pre = sums = [0] + nums
        for i in range(2, len(sums)):
            sums[i] += sums[i - 1]
        for k in range(2, m + 1):
            (i, j, cur) = (k - 1, k, [sys.maxsize] * len(pre))
            while j < len(pre):
                (left, right) = (pre[i], sums[j] - sums[i])
                cur[j] = min(cur[j], max(left, right))
                if i + 1 < j and max(pre[i + 1], sums[j] - sums[i + 1]) < cur[j]:
                    i += 1
                else:
                    j += 1
            pre = cur
        return pre[-1]

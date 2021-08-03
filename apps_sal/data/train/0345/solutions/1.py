class Solution:
    def splitArray(self, pages, k):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        if not pages or k == 0:
            return 0

        pre = sums = [0] + pages[:]
        for i in range(1, len(sums)):
            sums[i] += sums[i - 1]

        for n in range(2, k + 1):
            if n > len(pages):
                break

            cur = [sys.maxsize] * len(pre)
            i, j = n - 1, n
            while j < len(pre):
                left, right = pre[i], sums[j] - sums[i]
                cur[j] = min(cur[j], max(left, right))
                if i + 1 < j and max(pre[i + 1], sums[j] - sums[i + 1]) < cur[j]:
                    i += 1
                else:
                    j += 1

            pre = cur

        return pre[-1]

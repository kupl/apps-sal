class Solution:

    # space optimized
    def getMaxLen(self, nums: List[int]) -> int:

        ans = 0
        neg_pos = None
        neg_count = 0
        left = -1
        for i, n in enumerate(nums):
            if n == 0:
                neg_pos = None
                neg_count = 0
                left = i
                continue
            elif n > 0:
                if neg_count % 2 == 0:
                    ans = max(ans, i - left)
                else:
                    ans = max(ans, i - neg_pos)
            elif n < 0:
                neg_count += 1
                if neg_pos is None:
                    neg_pos = i
                if neg_count % 2 == 0:
                    ans = max(ans, i - left)
                else:
                    ans = max(ans, i - neg_pos)

        return ans

    # original O(n) space
    def getMaxLen1(self, nums: List[int]) -> int:

        ans = 0
        dq = []
        left = -1
        for i, n in enumerate(nums):
            if n == 0:
                dq.clear()
                left = i
                continue
            elif n > 0:
                if len(dq) % 2 == 0:
                    ans = max(ans, i - left)
                else:
                    ans = max(ans, i - dq[0])
            elif n < 0:
                dq.append(i)
                if len(dq) % 2 == 0:
                    ans = max(ans, i - left)
                else:
                    ans = max(ans, i - dq[0])

        return ans

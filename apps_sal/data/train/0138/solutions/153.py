class Solution:

    def getMaxLen(self, nums: List[int]) -> int:
        (res, n, q, cur) = (0, len(nums), [], 1)

        def extract(q, cur, res):
            if cur > 0:
                res = max(res, len(q))
            else:
                i = 0
                while i < len(q):
                    if q[i] < 0:
                        break
                    i += 1
                res = max(res, len(q) - i - 1)
                i = len(q) - 1
                while i >= 0:
                    if q[i] < 0:
                        break
                    i -= 1
                res = max(res, i)
            return res
        for v in nums:
            if v != 0:
                q.append(v)
                cur *= v
            else:
                res = extract(q, cur, res)
                cur = 1
                q = []
        return extract(q, cur, res)

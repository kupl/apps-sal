class Solution:
    def longestMountain(self, A: List[int]) -> int:
        res = cur = 1
        desc = False
        for i in range(1, len(A)):
            if A[i - 1] == A[i]:
                if desc:
                    res = max(res, cur)
                desc = False
                cur = 1
            elif A[i - 1] < A[i]:
                if not desc:
                    cur += 1
                else:
                    res = max(res, cur)
                    cur = 2
                    desc = False
            else:
                if desc:
                    cur += 1
                elif cur > 1:
                    desc = True
                    cur += 1
                else:
                    cur = 1
                    desc = False
        if desc:
            res = max(res, cur)
        return 0 if res < 3 and not desc else res

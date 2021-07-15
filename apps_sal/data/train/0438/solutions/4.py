class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        res = -1
        cnt = 0
        lm = {i: 0 for i in range(len(arr) + 2)}
        for i, idx in enumerate(arr):
            length = lm[idx - 1] + 1 + lm[idx + 1]
            if lm[idx - 1] == m:
                cnt -= 1
            if lm[idx + 1] == m:
                cnt -= 1
            if length == m:
                cnt += 1
            if cnt > 0:
                res = i + 1
            lm[idx - lm[idx - 1]] = length
            lm[idx + lm[idx + 1]] = length
        return res

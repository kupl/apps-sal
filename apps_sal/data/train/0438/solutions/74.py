class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:
        if len(arr) == m:
            return m
        length = [0] * (len(arr) + 2)
        cnt = [0] * (len(arr) + 1)
        res = -1
        for (idx, i) in enumerate(arr):
            l = length[i - 1]
            r = length[i + 1]
            length[i] = length[i - l] = length[i + r] = l + r + 1
            cnt[l] -= 1
            cnt[r] -= 1
            cnt[length[i]] += 1
            if cnt[m]:
                res = idx + 1
        return res

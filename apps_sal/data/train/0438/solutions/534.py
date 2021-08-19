class Solution:

    def findLatestStep(self, A: List[int], m: int) -> int:
        n = len(A)
        length = [0] * (n + 2)
        cnt = [0] * (n + 2)
        res = -1
        for (i, v) in enumerate(A):
            l = length[v - 1]
            r = length[v + 1]
            length[v] = length[v - l] = length[v + r] = l + r + 1
            cnt[l] -= 1
            cnt[r] -= 1
            cnt[l + r + 1] += 1
            if cnt[m] != 0:
                res = i + 1
        return res
